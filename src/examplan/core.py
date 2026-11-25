"""Split exam time across questions in proportion to their marks.

Time left after reading and review is shared by marks:
minutes for a question = working_time x marks / total_marks.
Everything is an exact Fraction, so the pieces add back to the whole.
"""
from fractions import Fraction


def minutes_per_mark(total_minutes, total_marks, reading=0, review=0):
    working = Fraction(total_minutes) - Fraction(reading) - Fraction(review)
    if total_marks <= 0:
        raise ValueError("total marks must be positive")
    if working <= 0:
        raise ValueError("no working time is left after reading and review")
    return working / total_marks


def plan(total_minutes, marks, reading=0, review=0, start_minute=0):
    """marks: list of marks per question. Returns a list of dicts with the
    start and end minute (from the start of the paper) and the minutes."""
    if not marks or any(m <= 0 for m in marks):
        raise ValueError("every question needs positive marks")
    rate = minutes_per_mark(total_minutes, sum(marks), reading, review)
    t = Fraction(start_minute) + Fraction(reading)
    rows = []
    for i, m in enumerate(marks, 1):
        d = rate * m
        rows.append({"question": i, "marks": m, "minutes": d, "start": t, "end": t + d})
        t += d
    return rows


def pace_status(rows, question, elapsed):
    """Minutes ahead (positive) or behind (negative) when question's work is done."""
    row = rows[question - 1]
    return row["end"] - Fraction(elapsed)


def _mmss(x):
    s = round(Fraction(x) * 60)
    return f"{s // 60}:{s % 60:02d}"


def format_plan(rows):
    lines = ["Q   marks  minutes  start  end"]
    for r in rows:
        lines.append(f"{r['question']:<3} {r['marks']:<6} {_mmss(r['minutes']):<8} {_mmss(r['start']):<6} {_mmss(r['end'])}")
    return "\n".join(lines)
