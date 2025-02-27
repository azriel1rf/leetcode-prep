from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cnt1 = defaultdict(int)
        cnt2 = defaultdict(int)
        for char in s:
            cnt1[char] += 1
        for char in t:
            cnt2[char] += 1
        for key in cnt1:
            if cnt1[key] != cnt2[key]:
                return False
        for key in cnt2:
            if cnt1[key] != cnt2[key]:
                return False
        return True
