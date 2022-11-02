# nums   = [1, 4, 3, -5, -4, 8, 6]
# def solve3(nums,n,i):
#     if i == n-1:
#         return nums[-1]
#     return max(nums[i],solve3(nums,n,i+1))
# print(solve3(nums,len(nums),0))
#
#
import sys
sys.setrecursionlimit(10**4)
class Solution:
    def numberOfSteps(self, num: int) -> int:
        def Solve(num, cnt):
            if num == 0:
                return cnt
            if not num % 2:
                return Solve(num // 2, cnt + 1)
            else:
                return Solve(num - 1, cnt + 1)

        return Solve(num, 0)
        

obj = Solution()
print(obj.numberOfSteps(1010201))