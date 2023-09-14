class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ss=''
        temp_ss=''
        for i in s:
            if i in temp_ss:
                if len(temp_ss)>len(ss):
                    ss=temp_ss
                temp_ss=temp_ss[temp_ss.index(i)+1:]+i
            else:
                temp_ss+=i
        if len(temp_ss)>len(ss):
            return len(temp_ss)
        return len(ss)

