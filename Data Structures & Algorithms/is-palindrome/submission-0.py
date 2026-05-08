class Solution:
    def isPalindrome(self, s: str) -> bool:
        G="".join(i.lower() for i in s if i.isalnum())
        K=G[::-1]
        print(K)
        if G==K:
            return True
        else:
            return False
    

        