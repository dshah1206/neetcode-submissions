class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """Sorting Approach
        T.C: O(NlogN), S.C: O(N)
        """
        # count = {}
        # for num in nums:
        #     count[num] = 1 + count.get(num, 0)
        
        # arr = []
        # for num, cnt in count.items():
        #     arr.append([cnt,num])
        # arr.sort()
        # print(arr)
        
        # res = []
        # while len(res) < k:
        #     res.append(arr.pop()[1])
        #     print(res)
        # return res

        """ Min-Heap
        T.C: O(NLogK), S.C: O(N+K)
        """
        # count = {}
        # for num in nums:
        #     count[num] = 1 + count.get(num, 0)
        
        # heap = []
        # for num in count.keys():
        #     heapq.heappush(heap, (count[num], num))
        #     if len(heap) > k:
        #         heapq.heappop(heap)
        # res = []
        # for _ in range(k):
        #     res.append(heapq.heappop(heap)[1])
        # return (res)

        """ Bucket Sort with modification: use freq as first to
        get number that occurred that many times      
        T.C - O(N), S.C - O(N)
        """
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        # if len = 6 the freq = [[],[],[],[],[],[],[]] because there   
        # will be no element with zero count
        freq = [[] for i in range(len(nums)+1)]

        for num, cnt in count.items():
            freq[cnt].append(num)
        res = []
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res


            


        




        
        