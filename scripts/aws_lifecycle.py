"""AWSライフサイクルの表示語彙。公式の掲載分類や名称は変更しない。"""


def lifecycle_label(stage, end="—"):
    """Render one pair of parentheses, with an optional ISO support-end date."""
    has_date = end not in ("", "—", None)
    if stage == "maintenance":
        detail = "新規利用に制限" + (f"、{end}サポート終了" if has_date else "")
        return f"Maintenance（{detail}）"
    if stage == "sunset":
        return f"Sunset（{end if has_date else ''}終了予定）"
    if stage == "shutdown":
        return f"Full Shutdown（{str(end)+'終了' if has_date else '終了済み'}）"
    raise ValueError("Unknown lifecycle stage: " + str(stage))


LIFECYCLE_LABELS = {stage: lifecycle_label(stage)
                    for stage in ("maintenance", "sunset", "shutdown")}
