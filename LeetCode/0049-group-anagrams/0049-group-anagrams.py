class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_dic= collections.defaultdict(list)
        for idx, word in enumerate(strs):
            sorted_word = ''.join(sorted(word))
            
            if strs_dic[sorted_word]:
                strs_dic[sorted_word].append(word)
            else:
                strs_dic[sorted_word] = [word]
        
        return list(strs_dic.values())