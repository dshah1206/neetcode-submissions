class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        def frequency(word:str):
            count = {}
            for char in word:
                if char not in count:
                    count[char] = 1
                else:
                    count[char] += 1
            return count

        s_count = frequency(s)
        t_count = frequency(t)
        
        return s_count == t_count

        
        
        