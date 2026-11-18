class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        nums = sorted(nums)
        
        length = len(nums) - 1

        output = []

        for target_i, target in enumerate(nums):

            if (target_i != 0 and target != nums[target_i - 1]) or target_i == 0:

                l = target_i + 1
                r = length

                while l < r:

                    ptr_sum = nums[l] + nums[r] + target

                    if ptr_sum == 0:

                        output.append([nums[l], nums[r], target])
                        l += 1
                        
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1


                    elif ptr_sum < 0:
                        l += 1
                    else:
                        r -= 1
                    
        return output
