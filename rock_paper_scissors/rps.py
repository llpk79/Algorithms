#!/usr/bin/python
import sys


def rock_paper_scissors(n):
    plays = ['rock', 'paper', 'scissors']
    return _rock_paper_scissors(n, plays, [])


def _rock_paper_scissors(n, plays, answer=None, final=None):
    final = [] if final is None else final
    if n == 0:
        final.append(answer)
        return [[]]
    for play in plays:
        new_ans = answer + [play]
        _rock_paper_scissors(n - 1, plays, new_ans, final)
    return final


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print(rock_paper_scissors(4))
