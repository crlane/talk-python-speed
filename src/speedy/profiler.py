import cProfile
import pstats

from speedy.main import longest_collatz
from speedy.mainx import longest_collatzx


def profile():
    cProfile.runctx("longest_collatz()", globals(), locals(), "CollatzProfile.prof")
    s = pstats.Stats("CollatzProfile.prof")
    s.strip_dirs().sort_stats("time").print_stats()

    cProfile.runctx("longest_collatzx()", globals(), locals(), "CollatzxProfile.prof")
    s = pstats.Stats("CollatzxProfile.prof")
    s.strip_dirs().sort_stats("time").print_stats()

if __name__ == '__main__':
    profile()
