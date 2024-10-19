class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s="0"
        for i in range(n-1):
            inverted=""
            for i in s:
                if i=="1":
                    inverted+="0"
                else:
                    inverted+="1"
            s=s+"1"+inverted[::-1]
        return s[k-1]

