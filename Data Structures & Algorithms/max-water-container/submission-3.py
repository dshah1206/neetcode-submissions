class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        T.C: O(N^2) S.C: O(1)
        """
        # area = 0
        # for i in range(len(heights)):
        #     for j in range(i,len(heights)):
        #         area = max(area,(j-i) * min(heights[i], heights[j]))
        # return area

        """
        T.C: O(N) S.C: O(1)
        """
        area = 0
        i = 0
        j = len(heights) - 1
        while i < j:
            area = max(area,(j-i) * min(heights[i], heights[j]))
            if heights[i] <= heights[j]:
                i += 1
            else:
                j -= 1
        return area
        