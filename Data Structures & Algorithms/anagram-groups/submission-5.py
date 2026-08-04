class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        char_count_map = defaultdict(list)

        for st in strs:
            char_count = [0] * 26
            for c in st:
                idx = ord(c) - ord("a")
                char_count[idx] += 1
            map_key = tuple(char_count)
            char_count_map[map_key].append(st)

        return list(char_count_map.values())