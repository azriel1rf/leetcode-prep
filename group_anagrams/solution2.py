from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            counts = [0] * 26
            for char in s:
                idx = ord(char) - ord("a")
                counts[idx] += 1
            groups[tuple(counts)].append(s)
        return list(groups.values())

