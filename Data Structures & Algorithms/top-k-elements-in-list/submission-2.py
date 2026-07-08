class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq_dict = defaultdict(int)

        for num in nums:
            freq_dict[num] += 1

        sorted_elements = sorted(freq_dict.keys(), key=lambda x: freq_dict[x], reverse=True)
        
        return sorted_elements[:k]