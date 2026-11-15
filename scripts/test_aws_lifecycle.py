#!/usr/bin/env python3
"""状態の表示語彙・日付・製品と関連サービスの境界を検証する。"""
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
    """取得スナップショットから再描画し、実際の検証スクリプトまで通す。"""

    ROOT = Path(__file__).resolve().parents[1]

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
            products_md = (work / "cloud/aws/products.md").read_text(encoding="utf-8")
            row = next(line for line in products_md.splitlines()
                       if line.startswith("| Amazon WorkSpaces Thin Client |"))
            return result, row

    def test_current_snapshot_day_is_reproduced(self):
        day = json.loads((self.ROOT / "cloud/aws/products-source.json")
                         .read_text(encoding="utf-8"))["retrieved_utc"]
        result, row = self.regenerate_and_check(day)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("[Sunset（2027-03-31終了予定）](lifecycle.md)", row)

    def test_snapshot_after_sunset_end_date_passes_checks(self):
        # 公式Sunset表に残ったまま終了日を過ぎても、更新Workflowの検証で止まらない。
        result, row = self.regenerate_and_check("2027-04-01")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("[Sunset（2027-03-31終了日経過・Full Shutdown未照合）](lifecycle.md)", row)


if __name__ == "__main__":
    unittest.main()
