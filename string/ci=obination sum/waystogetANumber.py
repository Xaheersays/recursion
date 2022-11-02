class Solution:
    def numRollsToTarget(self, n, k, target):
        ans = []
        def func(pro,ans,target):
            if target ==0 or target<0:
                ans.append(pro)
                return
            for i in range(1,k+1):
                if i <= target:
                    func(pro+str(i),ans,target-i)
        func("",ans,target)
        return ans,len(ans)

n = 2
k = 10
target =10
ob = Solution()
print(ob.numRollsToTarget(n,k,target))