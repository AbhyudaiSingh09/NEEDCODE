#Given an integer array nums and an integer k, return the k most frequent elements within the array.
#The test cases are generated such that the answer is always unique.
#You may return the output in any order.


from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums,k):
        freq_map = Counter(nums)

        for num,freq in freq_map:
            heap=[]
            heapq.heappush(heap,(freq,num))
            if len(heap)>k:
                heapq.heappop(heap)
        return [num for freq, num in heap]        
