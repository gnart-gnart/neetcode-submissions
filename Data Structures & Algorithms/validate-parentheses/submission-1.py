class Solution:
    def isValid(self, s: str) -> bool:

        def bracketsMatch(a: str, b: str) -> bool:
            if a == "{" and b == "}":
                return True
            if a == "["  and b == "]":
                return True
            if a == "(" and b == ")":
                return True
            return False

        stack = []
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                if bracketsMatch(stack[-1], c):
                    stack.pop()
                    continue
                else:
                    return False
        return len(stack) == 0