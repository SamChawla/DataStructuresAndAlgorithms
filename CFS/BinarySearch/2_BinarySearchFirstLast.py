# Practice Question: https://practice.geeksforgeeks.org/problems/first-and-last-occurrences-of-x3116/1/
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

#  Find position of first and last occurance of an element in a sorted array with possible duplicate values
# Return position values if found else -1 -1


class Solution:

    def findHelper(self, arr, K, first):
        left_index = 0
        right_index = len(arr) - 1
        mid_index = 0

        ans = -1

        while left_index <= right_index:
            # mid_index = (left_index + right_index) // 2  : Normal Way

            mid_index = left_index + (
                (right_index - left_index) // 2
            )  # To avoid overflow
            mid_number = arr[mid_index]

            if mid_number == K:
                ans = mid_index
                if first:
                    right_index = mid_index - 1
                else:
                    left_index = mid_index + 1
                continue

            if mid_number < K:
                left_index = mid_index + 1
            else:
                right_index = mid_index - 1
        return ans

    def find(self, arr, N, K):
        
        first = self.findHelper(arr, K, first=True)
        last = -1
        # If first occurance is not found, we do not need to find the last one
        if first > -1:
            last = self.findHelper(arr, K, first=False)

        return [first, last]


if __name__ == "__main__":
    sol = Solution()

    N = 7
    K = 5
    # Test Case 1 -> [4, 5]
    arr = [1, 2, 3, 4, 5, 5, 6]
    print(sol.find(arr, N, K)) 

    # Test Case 2 -> [4, 4]
    arr = [1, 2, 3, 4, 5, 6, 6]
    print(sol.find(arr, N, K)) 

    # Test Case 3 -> [-1, -1]
    arr = [1, 2, 3, 4, 6, 6, 7]
    print(sol.find(arr, N, K)) 

