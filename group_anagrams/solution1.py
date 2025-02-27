from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def count_chars(seq: str) -> tuple[int, ...]:
            counts = [0] * 26
            for char in seq:
                idx = ord(char) - ord("a")
                counts[idx] += 1
            return tuple(counts)
        # `char counts` (tuple) -> `list of strings`
        groups = defaultdict(list)
        for seq in strs:
            groups[count_chars(seq)].append(seq)
        return list(groups.values())

