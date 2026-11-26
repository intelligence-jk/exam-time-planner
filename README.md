# KAIROS: Knowing All Important Revision, Organised by Slot

Formerly `exam-time-planner`.

Splits exam time across questions in proportion to their marks, with time for reading and for a final review.

## What it solves
Students run out of time on the last questions because nobody decided in advance how long each deserved. Give the total minutes, the reading and review time and the marks per question, and the tool prints a clock plan. Pure Python 3.10+, standard library only.

## Example
```bash
python -m examplan 180 10 10 10 20 25 25
```
```
Q   marks  minutes  start  end
1   10     20:00    10:00  30:00
2   20     40:00    30:00  70:00
3   25     50:00    70:00  120:00
4   25     50:00    120:00 170:00
```
(Output pasted from a real run.)

## The maths behind it
Working time is T - R - V (total minus reading minus review). Minutes per mark is (T - R - V) / M where M is the total marks, and a question worth m marks gets m (T - R - V) / M minutes. Everything is an exact `Fraction`, so the pieces always add back to the working time; a paper of 100 minutes and three 1-mark questions gives 100/3 minutes each, shown as 33:20. Here: 160 / 80 = 2 minutes per mark, so a 25-mark question gets 50 minutes.

## Install and run
```bash
python -m pip install -e .
python -m pytest
```

## Licence
MIT. Made by Math & Myth (mathandmyth.ae): one to one maths mentoring, online, across the UAE.
