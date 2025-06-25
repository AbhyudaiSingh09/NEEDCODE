#Given an integer array nums and an integer k, return the k most frequent elements within the array.
#The test cases are generated such that the answer is always unique.
#You may return the output in any order.


from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums,k):
        freq_map = Counter(nums)

        for num, freq in freq_map.items():
            heap=[]
            heapq.heappush(heap,(freq,num))
            if len(heap)>k:
                heapq.heappop(heap)
        return [num for freq, num in heap]        

# 🔧 Test cases
sol = Solution()

# Test 1
nums1 = [1, 1, 1, 2, 2, 3]
k1 = 2
print("Test 1 Output:", sol.topKFrequent(nums1, k1))  # Expected: [1, 2]

# Test 2
nums2 = [1]
k2 = 1
print("Test 2 Output:", sol.topKFrequent(nums2, k2))  # Expected: [1]

