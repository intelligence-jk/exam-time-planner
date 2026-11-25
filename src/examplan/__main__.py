import sys
from fractions import Fraction
from .core import plan, format_plan


def main(argv=None):
    a = sys.argv[1:] if argv is None else argv
    # usage: TOTAL READING REVIEW MARKS...
    try:
        total, reading, review = (Fraction(x) for x in a[:3])
        marks = [int(x) for x in a[3:]]
        print(format_plan(plan(total, marks, reading, review)))
        return 0
    except (ValueError, IndexError) as e:
        print("error:", e)
        print("usage: python -m examplan TOTAL READING REVIEW MARKS...")
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
