class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        
        g=[]
        for i in range(0,n-2):
            if i>0 and nums[i]==nums[i-1]:continue
            j=i+1
            k=n-1
            while j<k:
                s=nums[i]+nums[j]+nums[k]
                if s==0:
                    g.append([nums[i],nums[j],nums[k]])
                    while j<k and nums[j]==nums[j+1]:
                        j=j+1
                    while j<k and nums[k]==nums[k-1]:
                        k=k-1
                    j=j+1
                    k=k-1
                elif s>0:
                    k=k-1
                else:
                    j=j+1
        if not g:
            return []
        return g

        