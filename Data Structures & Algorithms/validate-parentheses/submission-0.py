class Solution:
    def isValid(self, s: str) -> bool:

        """
        T.C: O(N) S.C: O(N)
        """
        stack = []
        for char in s:
            if char == "(" or char == "{" or char == "[":
                stack.append(char)
            elif stack == []:
                return False
            elif (char == ")" and stack.pop() != "(") or (char == "}" and stack.pop() != "{") or (char == "]" and stack.pop() != "["):
                return False
        if len(stack) == 0:
            return True
        return False
        