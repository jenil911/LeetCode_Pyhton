class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n == 1:
            return

        i = n - 2

        # this loop will find the pivot point
        while i >= 0 and nums[i + 1] <= nums[i]:
            i -= 1

        if i >= 0:
            j = n - 1

            while nums[j] <= nums[i]:
                j -= 1
            
            # Swap the considered element with next greater element in the subarray

            nums[i], nums[j] = nums[j], nums[i]

            # reverse the subarray
            self.reverse(nums, i + 1, n - 1)
        else:
            self.reverse(nums, 0, n - 1)

    # Method to reverse array
    def reverse(self, nums: List[int], start: int, end: int) -> None:
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1