# https://leetcode.com/problems/contains-duplicate/
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
# Input: nums = [1,2,3,1]
# Output: true

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False


if __name__ == "__main__":
    nums = [1,2,3,1]
    print(Solution().containsDuplicate(nums))