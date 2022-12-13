# https://practice.geeksforgeeks.org/problems/square-root/1

"""
Given an integer x, find the square root of x. If x is not a perfect square, then return floor(√x).

Input:
x = 5
Output: 2
Explanation: Since, 5 is not a perfect 
square, floor of square_root of 5 is 2.

"""

#User function Template for python3


#Complete this function
class Solution:
    def floorSqrt(self, x):
        if x ==1:
            return 1
        
        l = 0
        h = x//2
        ans = None
        
        while l <=h:
            mid = l + ((h-l)//2)
            
            sqr = mid * mid
            
            if sqr == x:
                return mid
            
            if sqr>x:
                h=mid-1
            else:
                ans = mid
                l=mid+1
        return ans


def main():

    sol = Solution()
    print(sol.floorSqrt(5))


if __name__ == "__main__":
    main()
