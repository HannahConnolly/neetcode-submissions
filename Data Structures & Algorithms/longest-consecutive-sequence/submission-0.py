class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:

        if not nums:
            return 0

        max_len = 1

        num_set = set()

        for num in nums:
            num_set.add(num)

        for num in num_set:
            if num - 1 not in num_set:

                i = 1

                while(num + i in num_set):

                    if i + 1 > max_len:
                        max_len = i + 1

                    i += 1
        
        return max_len