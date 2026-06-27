class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        l=0
        r=n-1
        lm=height[l]
        rm=height[r]
        g=0
        while l<r:
            if lm<rm:
                l+=1
                lm=max(height[l],lm)
                g+=lm-height[l]
            else:
                r-=1
                rm=max(height[r],rm)
                g+=rm-height[r]
        return g


        