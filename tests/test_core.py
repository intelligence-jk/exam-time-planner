from fractions import Fraction as F
import pytest
from examplan import plan, minutes_per_mark, pace_status, format_plan


def test_rate():
    assert minutes_per_mark(180, 80, reading=10, review=10) == F(2)


def test_plan_sums_to_working_time():
    rows = plan(180, [10, 20, 25, 25], reading=10, review=10)
    assert sum(r["minutes"] for r in rows) == 160


def test_plan_is_contiguous():
    rows = plan(120, [5, 7, 11], reading=5, review=10)
    assert rows[0]["start"] == 5
    for a, b in zip(rows, rows[1:]):
        assert a["end"] == b["start"]
    assert rows[-1]["end"] == 120 - 10


def test_exact_fraction_not_float():
    rows = plan(100, [1, 1, 1])
    assert rows[0]["minutes"] == F(100, 3)
    assert sum(r["minutes"] for r in rows) == 100


def test_proportional():
    rows = plan(90, [10, 20])
    assert rows[1]["minutes"] == 2 * rows[0]["minutes"]


def test_pace():
    rows = plan(120, [10, 10])
    assert pace_status(rows, 1, 50) == 10
    assert pace_status(rows, 2, 130) == -10


def test_start_offset():
    assert plan(60, [1], start_minute=540)[0]["start"] == 540


def test_bad_inputs():
    with pytest.raises(ValueError):
        plan(60, [])
    with pytest.raises(ValueError):
        plan(60, [5, 0])
    with pytest.raises(ValueError):
        plan(20, [5], reading=10, review=10)


def test_format():
    out = format_plan(plan(100, [1, 1, 1]))
    assert "33:20" in out and out.splitlines()[0].startswith("Q")
