# Practice Question: https://practice.geeksforgeeks.org/problems/who-will-win-1587115621/1/

#  Searching an element in a sorted array
# Return `1`` if K is found in array, else `-1``


class Solution:
    def searchInSorted(self, arr, N, K):
        left_index = 0
        right_index = len(arr) - 1
        mid_index = 0

        while left_index <= right_index:
            # mid_index = (left_index + right_index) // 2  : Normal Way

            mid_index = left_index + (
                (right_index - left_index) // 2
            )  # To avoid overflow
            mid_number = arr[mid_index]

            if mid_number == K:
                return 1

            if mid_number < K:
                left_index = mid_index + 1
            else:
                right_index = mid_index - 1

        return -1


if __name__ == "__main__":
    sol = Solution()

    arr = [1, 2, 3, 4, 6]
    N = 5
    K = 6

    print(sol.searchInSorted(arr, N, K))
