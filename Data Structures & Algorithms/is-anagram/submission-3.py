class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ans = False
        if (len(s) == len(t)):
            for cha in s:
                if (t.count(cha) == s.count(cha)):
                    ans = True
                else:
                    ans = False
                    break
        return ans