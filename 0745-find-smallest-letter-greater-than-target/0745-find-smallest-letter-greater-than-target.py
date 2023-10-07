class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        m=123
        smallest=letters[0]
        for i in letters:
            if ord(i)>ord(target) and ord(i)<m:
                m=ord(i)
            if ord(i)<ord(smallest):
                smallest=i
        if m==123:
            return smallest
        return chr(m)