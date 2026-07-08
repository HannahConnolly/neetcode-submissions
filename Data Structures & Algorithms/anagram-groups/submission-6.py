class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagram_dict = {}
        
        for str in strs:
            sorted_str = "".join(sorted(str))

            if sorted_str in anagram_dict:
                anagram_dict[sorted_str].append(str)

            else:
                anagram_dict[sorted_str] = [str]

        anagram_families = []
        
        for str_arr in anagram_dict:
            anagram_families.append(anagram_dict[str_arr])

        return anagram_families