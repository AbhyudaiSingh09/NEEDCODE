class Solution:
    def numDecodings(self, s: str) -> int:
        # Memo: ways to decode starting at index i
        dp = {len(s): 1}

        def dfs(i: int) -> int:
            if i in dp:
                return dp[i]
            if s[i] == "0":
                return 0

            # Take one digit
            res = dfs(i + 1)

            # Take two digits if valid (10–26)
            if (
                i + 1 < len(s)
                and (
                    s[i] == "1"
                    or (s[i] == "2" and s[i + 1] in "0123456")
                )
            ):
                res += dfs(i + 2)

            dp[i] = res
            return res

        return dfs(0)
    
solver = Solution()
result = solver.numDecodings("226")
print(result)

