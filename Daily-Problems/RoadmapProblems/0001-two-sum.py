# https://leetcode.com/problems/two-sum/
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        target_list = {} # store index using value as key
        for i,val in enumerate(nums):
            complement = target - val
            if complement in target_list:
                return [target_list[complement],i]
            target_list[val] = i


if __name__ == "__main__":
    nums = [2,7,11,15]
    print(Solution().twoSum(nums,9))