class Solution:
    def isValid(self, s: str) -> bool:
        bracket_dict = {
            "[":"]",
            "{":"}",
            "(":")"
        }

        stack = []
        for i in s:
            if i in bracket_dict:
                stack.append(bracket_dict[i])
            else:
                if not stack or stack[-1] != i:
                    return False
                stack.pop()
        return not stack
    
s = "[]"
test= Solution()

print(test.isValid("()[]{}"))  
