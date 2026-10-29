class Solution:
    def trap(self, height: List[int]) -> int:
        """
        T.C: O(N^2), S.C: O(1) - Brute Approach
        """
        # if not height:
        #     return 0
        
        # n = len(height)
        # res = 0

        # for i in range(n):
        #     leftmax = rightmax = height[i]

        #     for l in range(i):
        #         leftmax = max(leftmax, height[l])
            
        #     for r in range(i+1, n):
        #         rightmax = max(rightmax, height[r])
            
        #     res += min(leftmax, rightmax) - height[i]
    
        # return res

        """
        T.C: O(N), S.C: O(N) - Prefix & Suffix Approach
        """
        if not height:
            return 0

        n = len(height)
        leftmax = [0] * n
        rightmax = [0] * n

        leftmax[0] = height[0]
        for i in range(1,n):
            leftmax[i] = max(leftmax[i-1], height[i])

        rightmax[n-1] = height[n-1]
        for i in range(n-2,-1,-1):
            rightmax[i] = max(rightmax[i+1], height[i])

        res = 0
        for i in range(n):
            res += min(leftmax[i], rightmax[i]) - height[i]
        
        return res

        """
        T.C: O(N), S.C: O(1) - Two Pointer Approach
        """
        # if not height:
        #     return 0
        # l, r = 0, len(height) - 1
        # leftmax = height[l]
        # rightmax = height[r]
        # res = 0

        # while l<r:
        #     if leftmax <= rightmax:
        #         l += 1
        #         leftmax = max(leftmax, height[l])
        #         res += leftmax - height[l]
        #     else:
        #         r -= 1
        #         rightmax = max(rightmax, height[r])
        #         res += rightmax - height[r]

        # return res





        

        