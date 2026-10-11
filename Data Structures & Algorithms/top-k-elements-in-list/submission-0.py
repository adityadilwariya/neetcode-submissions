from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts=Counter(nums)
        final_key=[key for key, count in counts.most_common(k)]
        return (final_key)
