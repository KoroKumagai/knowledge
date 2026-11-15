#!/usr/bin/env python3
"""状態の表示語彙・日付・製品と関連サービスの境界を検証する。"""
from pathlib import Path
import sys
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


if __name__ == "__main__":
    unittest.main()
