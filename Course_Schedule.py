
class Solution:
    def numDecodings(self, s: str) -> int:
        dp ={len(s):1}

        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i]=="0":
                return 0 
            res = dfs(i+1)
            if(i +1< len(s) and (s[i] == "1" or s[i]=="2" and s[i+1] in "0123456")):
                res += dfs(i+2)
            dp[i] = res
            return res
        return dfs(0)
    
# test_num_decodings.py
# test_num_decodings.py
import pytest

from solution import Solution  # adjust if your file is named differently

@pytest.mark.parametrize("s,expected", [
    # Basic
    ("1", 1),
    ("12", 2),           # "AB", "L"
    ("226", 3),          # "2 2 6", "22 6", "2 26"
    ("2263", 3),         # "226" (3 ways) * "3" (1 way) => 3

    # Zeros & invalid pairs
    ("0", 0),
    ("06", 0),
    ("10", 1),           # "J"
    ("101", 1),          # "10 1"
    ("100", 0),          # "10 0" invalid
    ("301", 0),          # "30" invalid

    # Boundaries around 26
    ("27", 1),           # only "2 7"
    ("2101", 1),         # "2 10 1"
    ("11106", 2),        # typical tricky case -> 2

    # Edge / special
    ("", 1),             # With THIS implementation, empty string returns 1 (base dp[n]=1)
])
def test_num_decodings_parametrized(s, expected):
    assert Solution().numDecodings(s) == expected


def test_long_valid_run():
    # Many single-digit decodes, no 0s; Fibonacci-like growth check on a modest length.
    s = "111111"  # length 6 -> ways = F(7) = 13
    assert Solution().numDecodings(s) == 13# test_num_decodings.py
import pytest

from solution import Solution  # adjust if your file is named differently

@pytest.mark.parametrize("s,expected", [
    # Basic
    ("1", 1),
    ("12", 2),           # "AB", "L"
    ("226", 3),          # "2 2 6", "22 6", "2 26"
    ("2263", 3),         # "226" (3 ways) * "3" (1 way) => 3

    # Zeros & invalid pairs
    ("0", 0),
    ("06", 0),
    ("10", 1),           # "J"
    ("101", 1),          # "10 1"
    ("100", 0),          # "10 0" invalid
    ("301", 0),          # "30" invalid

    # Boundaries around 26
    ("27", 1),           # only "2 7"
    ("2101", 1),         # "2 10 1"
    ("11106", 2),        # typical tricky case -> 2

    # Edge / special
    ("", 1),             # With THIS implementation, empty string returns 1 (base dp[n]=1)
])
def test_num_decodings_parametrized(s, expected):
    assert Solution().numDecodings(s) == expected


def test_long_valid_run():
    # Many single-digit decodes, no 0s; Fibonacci-like growth check on a modest length.
    s = "111111"  # length 6 -> ways = F(7) = 13
    assert Solution().numDecodings(s) == 13

@pytest.mark.parametrize("s,expected", [
    # Basic
    ("1", 1),
    ("12", 2),           # "AB", "L"
    ("226", 3),          # "2 2 6", "22 6", "2 26"
    ("2263", 3),         # "226" (3 ways) * "3" (1 way) => 3

    # Zeros & invalid pairs
    ("0", 0),
    ("06", 0),
    ("10", 1),           # "J"
    ("101", 1),          # "10 1"
    ("100", 0),          # "10 0" invalid
    ("301", 0),          # "30" invalid

    # Boundaries around 26
    ("27", 1),           # only "2 7"
    ("2101", 1),         # "2 10 1"
    ("11106", 2),        # typical tricky case -> 2

    # Edge / special
    ("", 1),             # With THIS implementation, empty string returns 1 (base dp[n]=1)
])
def test_num_decodings_parametrized(s, expected):
    assert Solution().numDecodings(s) == expected


def test_long_valid_run():
    # Many single-digit decodes, no 0s; Fibonacci-like growth check on a modest length.
    s = "111111"  # length 6 -> ways = F(7) = 13
    assert Solution().numDecodings(s) == 13