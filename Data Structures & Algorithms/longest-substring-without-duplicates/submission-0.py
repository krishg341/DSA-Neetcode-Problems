class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        K={}
        l=0
        G=0
        for k,g in enumerate(s):
            if g in K and l<=K[g]:
                l=K[g]+1
            K[g]=k
            G=max(G,k-l+1)
        return G
            
            

            



        