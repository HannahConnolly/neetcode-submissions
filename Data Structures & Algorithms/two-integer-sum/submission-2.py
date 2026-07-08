class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        if len(nums) < 2:
            return False

        num_set, i = {}, 0 

        for num in nums:
            
            if target - num in num_set:
                return [num_set.get(target - num), i] 
            
            num_set[num] = i
            i += 1

        return [0, 0]