class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        char_count_dict = defaultdict(list)

        for st in strs:
            counts = [0] * 26
            
            for c in st:
                ord_idx = ord(c) - ord("a")
                counts[ord_idx] += 1
            count_tuple = tuple(counts)
            char_count_dict[count_tuple].append(st)
        
        return list(char_count_dict.values())