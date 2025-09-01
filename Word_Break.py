# test_word_break.py
# import pytest

# If Solution is defined in another file, e.g., solution.py:
# from solution import Solution

# If you're keeping tests in the same file/project, you can paste your Solution
# here or ensure the import above is correct.
class Solution:
    def wordBreak(self, s, wordDict):
        dp = [False] * (len(s)+1)
        dp[len(s)] = True
        for i in range(len(s)-1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i:i+len(w)] == w:
                    dp[i] = dp[i + len(w)]
                    if dp[i]:
                        break
        return dp[0]
    

test = Solution()
test.wordBreak("leetcode", ["leet", "code"])

# @pytest.mark.parametrize(
#     "s,wordDict,expected",
#     [
#         # Basic truths
#         ("leetcode", ["leet", "code"], True),
#         ("applepenapple", ["apple", "pen"], True),

#         # Basic falses / tricky gaps
#         ("catsandog", ["cats", "dog", "sand", "and", "cat"], False),
#         ("aaaaab", ["a", "aa", "aaa", "aaaa", "aaaaa"], False),

#         # Overlaps / multiple segmentations
#         ("aaaaaaa", ["aaaa", "aaa"], True),              # 4+3 or 3+4
#         ("cars", ["car", "ca", "rs"], True),             # "car" + "s" impossible, but "ca"+"rs" works

#         # Small inputs
#         ("", ["a", "b"], True),                          # empty string is segmentable
#         ("a", [], False),                                # no words
#         ("b", ["b"], True),
#         ("b", ["a"], False),

#         # Order independence (same set, diff order, same result)
#         ("leetcode", ["code", "leet"], True),

#         # Reuse words / repetition
#         ("aaaaaa", ["a", "aa", "aaa"], True),

#         # Unicode (if your function treats Unicode like normal strings, this should pass)
#         ("你好世界你好", ["你好", "世界"], True),

#         # Edge: dict contains s itself
#         ("hello", ["hell", "hello"], True),

#         # Edge: dict contains prefixes that cause backtracking
#         ("abcd", ["a", "abc", "b", "cd"], True),

#         # Edge: single char dictionary vs longer string
#         ("abc", ["a", "b", "ab"], False),  # missing "c"

#         # Regression-like examples
#         ("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"], True),
#         ("bb", ["a", "b", "bbb", "bbbb"], True),
#     ],
#     ids=[
#         "basic_true_leetcode",
#         "reuse_words_true",
#         "tricky_false_gap",
#         "suffix_mismatch_false",
#         "overlap_true",
#         "multi_seg_true",
#         "empty_string_true",
#         "no_words_false",
#         "single_char_true",
#         "single_char_false",
#         "order_independent_true",
#         "repetition_true",
#         "unicode_true",
#         "dict_contains_s_true",
#         "prefix_backtrack_true",
#         "missing_final_piece_false",
#         "complex_true",
#         "small_true",
#     ],
# )
# def test_word_break(s, wordDict, expected):
#     assert Solution().wordBreak(s, wordDict) == expected


# def test_large_negative_performance():
#     """
#     Large negative case: 'a'*10000 + 'b' cannot be segmented
#     with only 'a' blocks. This also sanity-checks performance.
#     """
#     s = "a" * 10000 + "b"
#     wordDict = ["a", "aa", "aaa", "aaaa", "aaaaa"]
#     assert Solution().wordBreak(s, wordDict) is False


# def test_large_positive_performance():
#     """
#     Large positive case: 'a'*10000 can be segmented using 'aaaa'
#     """
#     s = "a" * 10000
#     wordDict = ["aaaa"]
#     assert Solution().wordBreak(s, wordDict) is True