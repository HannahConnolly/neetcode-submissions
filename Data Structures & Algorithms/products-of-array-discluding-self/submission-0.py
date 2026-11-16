class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:

        length = len(nums)
        l, r = 1, length - 2

        result = [1] * length
        r_prod = 1

        # left product (start on second index)
        while l < length:

            result[l] = result[l - 1] * nums[l - 1]
            l += 1

        # right product (start on second to last index)
        # finalize prods
        r = length - 2
        while r >= 0:
            r_prod = r_prod * nums[r + 1]
            result[r] = result[r] * r_prod
            r -= 1

        return result


