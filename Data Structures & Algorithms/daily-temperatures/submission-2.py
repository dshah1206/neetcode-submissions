class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        T.C: O(N^2), S.C: O(1) - Brute Force
        """
        # n = len(temperatures)
        # result = []
        
        # for i in range(n):
        #     count = 1
        #     found = False
        #     for j in range(i+1, n):
        #         if temperatures[i] < temperatures[j]:
        #             found = True
        #             break
        #         count += 1
        #     count = 0 if not found else count
        #     result.append(count)
        # return result

        """
        T.C: O(N), S.C: O(N) - Stack
        """

        n = len(temperatures)
        result = [0] * n
        stack = []

        for index, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                st, si = stack.pop()
                result[si] = index - si
            stack.append((temp, index))
        
        return result




