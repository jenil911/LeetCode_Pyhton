from heapq import heappush, heappop
from typing import List

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        # Priority queue (min-heap) to store pairs of (value, index)
        pq = []
        for i, num in enumerate(nums):
            heappush(pq, (num, i))

        # Perform k operations
        while k > 0:
            value, idx = heappop(pq)  # Get the smallest element
            value *= multiplier       # Multiply the value
            heappush(pq, (value, idx))  # Push it back to the heap
            k -= 1

        # Update the original array with the final values from the heap
        while pq:
            value, idx = heappop(pq)
            nums[idx] = value

        return nums