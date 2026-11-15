"""AWSライフサイクルの表示語彙。公式の掲載分類や名称は変更しない。"""
from datetime import date

# 公式Sunset表に残ったまま終了日を過ぎた項目。推測でFull Shutdownへ再分類しない。
EXPIRED_SUNSET_LABEL = "Sunset（終了日経過・Full Shutdown未照合）"


def sunset_expired(end, as_of):
    """True when an ISO support-end date is on or before the as-of date."""
    if as_of is None or end in ("", "—", None):
        return False
    try:
        return date.fromisoformat(str(end)) <= date.fromisoformat(str(as_of))
    except ValueError:
        return False


def lifecycle_label(stage, end="—", as_of=None):
    """Render one pair of parentheses, with an optional ISO support-end date.

    as_of (ISO date, e.g. the snapshot retrieval day) keeps a past Sunset date
    from being shown as "終了予定". Without it, the label is time-independent.
    """
    has_date = end not in ("", "—", None)
    if stage == "maintenance":
        detail = "新規利用に制限" + (f"、{end}サポート終了" if has_date else "")
        return f"Maintenance（{detail}）"
    if stage == "sunset":
        if sunset_expired(end, as_of):
            return f"Sunset（{end}終了日経過・Full Shutdown未照合）"
        return f"Sunset（{end if has_date else ''}終了予定）"
    if stage == "shutdown":
        return f"Full Shutdown（{str(end)+'終了' if has_date else '終了済み'}）"
    raise ValueError("Unknown lifecycle stage: " + str(stage))


LIFECYCLE_LABELS = {stage: lifecycle_label(stage)
                    for stage in ("maintenance", "sunset", "shutdown")}
