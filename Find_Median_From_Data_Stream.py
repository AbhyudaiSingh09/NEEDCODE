# import heapq
# class MedianFinder:

#     def __init__(self):
#         self.lower_half, self.upper_half = [],[]

#     def addNum(self, num: int) -> None:
#         heapq.heappush(self.lower_half,-num)
#         heapq.heappush(self.upper_half,-heapq.heappop(self.lower_half))
#         if len(self.upper_half)>len(self.lower_half):
#             heapq.heappush(self.lower_half,-heapq.heappop(self.upper_half))

#     def findMedian(self) -> float:
#         if len(self.lower_half)> len(self.upper_half):
#             return -self.lower_half[0]
#         else:
#             return (-self.lower_half[0]+ self.upper_half[0])/2.0
        



import heapq

nums = [5, 3, 8, 1]
heapq.heapify(nums)       # turn list into min-heap
print(nums)               # [1, 3, 8, 5] (internally heapified)
print(heapq.heappop(nums))  # 1 (smallest element)