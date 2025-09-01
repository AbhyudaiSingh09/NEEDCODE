import pytest
from solution import Solution  # adjust if your file is named differently

@pytest.mark.parametrize("s,expected", [
    # Basic
    ("1", 1),
    ("12", 2),            # "AB", "L"
    ("226", 3),           # "2 2 6", "22 6", "2 26"
    ("2263", 3),          # 3 ways for "226" then "3"

    # Zeros & invalid pairs
    ("0", 0),
    ("06", 0),
    ("10", 1),            # "J"
    ("101", 1),           # "10 1"
    ("100", 0),           # "10 0" invalid
    ("301", 0),           # "30" invalid

    # Boundaries around 26
    ("27", 1),            # only "2 7"
    ("2101", 1),          # "2 10 1"
    ("11106", 2),         # classic tricky case

    # Edge / special
    ("", 1),              # this implementation returns 1 for empty (dp[n] = 1)
])
def test_num_decodings_parametrized(s, expected):
    assert Solution().numDecodings(s) == expected


def test_long_valid_run():
    # Many '1's -> Fibonacci-like growth: len=6 -> F(7)=13
    s = "111111"
    assert Solution().numDecodings(s) == 13