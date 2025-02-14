class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_dic= collections.defaultdict(list)
        
        for word in strs:
            strs_dic[''.join(sorted(word))].append(word)
        
        return list(strs_dic.values())