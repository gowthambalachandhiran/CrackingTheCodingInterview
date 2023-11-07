class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        counter = {}
        for pat,word in zip(pattern,s):
            if pat not in counter:
                counter[pat] = word
            if len(set(pattern)) != len(set(s)):
                return False
            if counter[pat] != word:
                return False
            if len(pattern) != len(s):
                return False
        return True