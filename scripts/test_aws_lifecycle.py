#!/usr/bin/env python3
"""状態の表示語彙・日付・製品と関連サービスの境界を検証する。"""
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parent))
from aws_lifecycle import lifecycle_label
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


if __name__ == "__main__":
    unittest.main()
