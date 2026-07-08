class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        s_dict, t_dict = {}, {}
        for ch in s:
            s_dict[ch] = s_dict.get(ch, 0) + 1
        
        for ch in t:
            t_dict[ch] = t_dict.get(ch, 0) + 1
            
        return t_dict == s_dict

# Time Complexity
# O(n) - loops over each dict once

# Space complexity
# O(1) - 1 dict per array with a max of 26 letters