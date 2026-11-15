#!/usr/bin/env python3
"""判定表と対象外注記の整合性を検証するオフライン回帰テスト。"""
from collections import Counter
from copy import deepcopy
from pathlib import Path
import re
import sys
import unittest

# Allow `python -m unittest` from the repository root as well as direct execution.
sys.path.insert(0, str(Path(__file__).resolve().parent))
import check_aws_audit_decisions as audit  # noqa: E402


class ExclusionBreakdownTest(unittest.TestCase):
    def setUp(self):
        self.state, self.count, _, _ = audit.audit()

    def assert_breakdown(self, state, count):
        text = audit.render(state, count, [])
        table = [line.split("|")[1:-1] for line in text.splitlines()
                 if line.startswith("| ")][1:8]
        notes = [line for line in text.splitlines() if line.startswith("> - ")]
        self.assertEqual(len(table), len(audit.DIM))
        self.assertEqual(len(notes), len(audit.DIM))
        for dim, row, note in zip(audit.DIM, table, notes):
            with self.subTest(dim=dim):
                expected = Counter(item["status"][dim] for item in state["records"]
                                   if item["status"][dim].startswith("対象外"))
                actual = {"対象外（"+label+"）": int(n) for label, n in
                          re.findall(r"([^：＋＝（]+?)(\d+)件(?=[＋＝])", note)}
                self.assertEqual(actual, dict(expected))
                total = sum(expected.values())
                self.assertEqual(int(row[3]), total)
                self.assertEqual(note.split("：", 1)[0], "> - "+row[0].strip())
                self.assertTrue(note.endswith("＝"+str(total)+"件") if total
                                else note.endswith("なし（0件）"))
                order = [s for s in state["status_values"] if s in expected]
                labels = re.findall(r"([^：＋＝（]+?)\d+件(?=[＋＝])", note)
                self.assertEqual(["対象外（"+label+"）" for label in labels], order)

    def test_current_data_and_chime_sdk(self):
        self.assert_breakdown(self.state, self.count)
        chime = next(item for item in self.state["records"]
                     if item["name"] == "Amazon Chime SDK")
        self.assertEqual(chime["status"], dict.fromkeys(audit.DIM, "未確認"))

    def test_changed_counts_and_dimension_specific_categories(self):
        state = deepcopy(self.state)
        # 描画専用の合成データ。次元ごとに件数・種別を変え、0件も含める。
        categories = ("対象外（ツール）", "対象外（終了済み）",
                      "対象外（物理端末）", "対象外（グローバル）")
        for i, item in enumerate(state["records"]):
            for j, dim in enumerate(audit.DIM):
                item["status"][dim] = categories[(i+j) % len(categories)] if i < j else "未確認"
        count = Counter((dim, status) for item in state["records"]
                        for dim, status in item["status"].items())
        self.assert_breakdown(state, count)

    def test_no_exclusions(self):
        state = deepcopy(self.state)
        for item in state["records"]:
            item["status"] = dict.fromkeys(audit.DIM, "未確認")
        count = Counter({(dim, "未確認"): len(state["records"]) for dim in audit.DIM})
        self.assert_breakdown(state, count)


if __name__ == "__main__":
    unittest.main()
