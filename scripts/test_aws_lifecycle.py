#!/usr/bin/env python3
"""状態の表示語彙・日付・製品と関連サービスの境界を検証する。"""
from datetime import date, timedelta
from pathlib import Path
import json
import shutil
import subprocess
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parent))
from aws_lifecycle import EXPIRED_SUNSET_LABEL, lifecycle_label
from refresh_aws_marketing_products import lifecycle_coverage_note, product_lifecycle


class LifecycleLabelTest(unittest.TestCase):
    def test_labels_with_and_without_dates(self):
        for stage, plain, dated in (
            ("maintenance", "Maintenance（新規利用に制限）",
             "Maintenance（新規利用に制限、2027-04-30サポート終了）"),
            ("sunset", "Sunset（終了予定）", "Sunset（2027-04-30終了予定）"),
            ("shutdown", "Full Shutdown（終了済み）", "Full Shutdown（2027-04-30終了）"),
        ):
            for end, expected in (("—", plain), ("2027-04-30", dated)):
                with self.subTest(stage=stage, end=end):
                    row = {"stage": stage, "end": end}
                    self.assertEqual(lifecycle_label(stage, end), expected)
                    self.assertEqual(lifecycle_coverage_note(row), expected)
                    own, records = product_lifecycle("Example", {}, {"Example": [row]})
                    self.assertEqual(own, f"[{expected}](lifecycle.md)")
                    self.assertEqual(records, [row])
                    related, records = product_lifecycle("Parent", {
                        "lifecycle_related": {"Parent": {"service": "Example"}}
                    }, {"Example": [row]})
                    self.assertEqual(related, f"[関連サービスの{expected}：Example](lifecycle.md)。"
                                     "製品本体の提供状態とは区別")
                    self.assertEqual(records, [])

    def test_sunset_past_end_date_is_not_shown_as_planned(self):
        # 公式Sunset表に残ったまま終了日を過ぎても「終了予定」と表示しない。
        expired = "Sunset（2027-03-31終了日経過・Full Shutdown未照合）"
        for as_of, expected in ((None, "Sunset（2027-03-31終了予定）"),
                                ("2027-03-30", "Sunset（2027-03-31終了予定）"),
                                ("2027-03-31", expired),
                                ("2027-04-01", expired)):
            with self.subTest(as_of=as_of):
                row = {"stage": "sunset", "end": "2027-03-31"}
                self.assertEqual(lifecycle_label("sunset", "2027-03-31", as_of), expected)
                own, records = product_lifecycle("Example", {}, {"Example": [row]}, as_of)
                self.assertEqual(own, f"[{expected}](lifecycle.md)")
                self.assertEqual(records, [row])
                related, _ = product_lifecycle("Parent", {
                    "lifecycle_related": {"Parent": {"service": "Example"}}
                }, {"Example": [row]}, as_of)
                self.assertIn(f"[関連サービスの{expected}：Example]", related)
        # 経過後も公式分類（Sunset）のまま。Full Shutdownへ推測で移さない。
        self.assertTrue(expired.startswith("Sunset（"))
        self.assertTrue(EXPIRED_SUNSET_LABEL.startswith("Sunset（"))
        self.assertEqual(lifecycle_label("sunset", "—", "2027-04-01"), "Sunset（終了予定）")

    def test_as_of_does_not_change_other_stages(self):
        for stage in ("maintenance", "shutdown"):
            with self.subTest(stage=stage):
                self.assertEqual(lifecycle_label(stage, "2025-01-29", "2027-04-01"),
                                 lifecycle_label(stage, "2025-01-29"))


REGENERATE = """
import json, sys
from pathlib import Path
root = Path(sys.argv[1]); day = sys.argv[2]
sys.path.insert(0, str(root / "scripts"))
import refresh_aws_marketing_products as g
aws = root / "cloud/aws"
source = json.loads((aws / "products-source.json").read_text(encoding="utf-8"))
config = json.loads((aws / "products-mapping.json").read_text(encoding="utf-8"))
products_md, coverage_md, _, _ = g.render(source["products"], g.get_general_reference(), config, day)
source["retrieved_utc"] = day
(aws / "products-source.json").write_text(json.dumps(source, ensure_ascii=False, indent=2) + "\\n", encoding="utf-8")
(aws / "products.md").write_text(products_md, encoding="utf-8")
(aws / "products-coverage.md").write_text(coverage_md, encoding="utf-8")
"""


class RegenerateAndCheckTest(unittest.TestCase):
    """取得スナップショットから再描画し、実際の検証スクリプトまで通す。

    期待値に製品名・日付を直書きしない。スナップショット更新後もそのまま使える。
    """

    ROOT = Path(__file__).resolve().parents[1]
    AWS = ROOT / "cloud/aws"

    def regenerate_and_check(self, day):
        with tempfile.TemporaryDirectory() as tmp:
            work = Path(tmp)
            for name in ("cloud", "scripts"):
                shutil.copytree(self.ROOT / name, work / name,
                                ignore=shutil.ignore_patterns("__pycache__"))
            subprocess.run([sys.executable, "-I", "-c", REGENERATE, str(work), day],
                           check=True, capture_output=True, text=True)
            result = subprocess.run(
                [sys.executable, str(work / "scripts/check_aws_marketing_products.py")],
                capture_output=True, text=True)
            rendered = {name: (work / "cloud/aws" / name).read_text(encoding="utf-8")
                        for name in ("products.md", "products-coverage.md")}
            return result, rendered

    def sunset_product(self):
        """公式Sunset表にサービス本体が一致し、ISO形式の終了日を持つ製品を1件選ぶ。"""
        import refresh_aws_marketing_products as generator
        source = json.loads((self.AWS / "products-source.json").read_text(encoding="utf-8"))
        config = json.loads((self.AWS / "products-mapping.json").read_text(encoding="utf-8"))
        byname = generator.read_product_lifecycle()
        for product in sorted(source["products"], key=lambda p: p["name"]):
            _, rows = generator.product_lifecycle(product["name"], config, byname)
            for row in rows:
                if row["stage"] == "sunset":
                    try:
                        return product["name"], date.fromisoformat(row["end"])
                    except ValueError:
                        continue
        self.skipTest("No Product matches a dated official Sunset entry")

    def test_current_snapshot_is_reproduced(self):
        # 保存済みの取得日で再描画した結果が、コミット済みの生成物と一致する。
        day = json.loads((self.AWS / "products-source.json")
                         .read_text(encoding="utf-8"))["retrieved_utc"]
        result, rendered = self.regenerate_and_check(day)
        self.assertEqual(result.returncode, 0, result.stderr)
        for name, text in rendered.items():
            with self.subTest(file=name):
                self.assertEqual(text, (self.AWS / name).read_text(encoding="utf-8"))

    def test_sunset_before_and_after_end_date_pass_checks(self):
        # 基準日は公式の終了日の前日・翌日に固定する（保存済みの取得日には依存しない）。
        # 公式Sunset表に残ったまま終了日を過ぎても、更新Workflowの検証で止まらない。
        name, end = self.sunset_product()
        for day, label in (
            (end - timedelta(days=1), f"Sunset（{end.isoformat()}終了予定）"),
            (end + timedelta(days=1), f"Sunset（{end.isoformat()}終了日経過・Full Shutdown未照合）"),
        ):
            with self.subTest(product=name, day=day.isoformat()):
                result, rendered = self.regenerate_and_check(day.isoformat())
                self.assertEqual(result.returncode, 0, result.stderr)
                row = next(line for line in rendered["products.md"].splitlines()
                           if line.startswith("| " + name + " |"))
                self.assertIn(f"[{label}](lifecycle.md)", row)

if __name__ == "__main__":
    unittest.main()
