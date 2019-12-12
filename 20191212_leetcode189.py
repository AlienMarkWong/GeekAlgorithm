from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        actual_rotate = k % len(nums)
        nums[:] = nums[-actual_rotate:]+ nums[:-actual_rotate]

    def rotate2(self, nums: List[int], k: int) -> None:
        for _ in range(k):
            nums.insert(0, nums.pop(-1))

    def rotate3(self, nums: List[int], k: int) -> None:
        """copy"""
        k = k % len(nums)
        count = 0
        start = 0
        while count < len(nums):
            current = start
            prev = nums[start]
            while True:
                next = (current + k) % len(nums)
                temp = nums[next]
                nums[next] = prev
                prev = temp
                current = next
                count += 1
                if current == start:
                    break
            start += 1

    def reverse(self, nums, start, end):
        """copy"""
        while (start < end):
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
            
    def rotate4(self, nums: List[int], k: int) -> None:
        """copy"""
        k = k % len(nums)
        self.reverse(nums, 0, len(nums) - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, len(nums) - 1)
