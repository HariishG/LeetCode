class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        shift_amount=[0 for _ in range(len(s)+1)]
        for i in shifts:
            if i[2]==1:
                shift_amount[i[0]]+=1
                shift_amount[i[1]+1]-=1
            else:
                shift_amount[i[0]]-=1
                shift_amount[i[1]+1]+=1
        total=0
        # print(shift_amount)
        for i in range(len(s)):
            total+=shift_amount[i]
            sa=97+(ord(s[i])+total-97)%26
            s = s[:i] + chr(sa) + s[i+1:]
        return s