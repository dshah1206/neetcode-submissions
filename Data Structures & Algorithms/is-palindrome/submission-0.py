class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        T.C: O(N) & S.C: O(N)
        """
        # newStr = ""
        # for char in s:
        #     if char.isalnum():
        #         newStr += char.lower()
        # print(newStr)
        # return newStr == newStr[::-1]

        """
        T.C: O(N) & S.C: O(1)
        """

        l = 0
        r = len(s) - 1

        while l<r:
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while l<r and not self.alphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
        
    def alphaNum(self, char):
        return (    
            ord('a') <= ord(char) <= ord('z') or 
            ord('A') <= ord(char) <= ord('Z') or 
            ord('0') <= ord(char) <= ord('9')
        )