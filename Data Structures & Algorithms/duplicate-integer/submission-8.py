class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numCount = defaultdict(int)
        for i in range(len(nums)):
            numCount[nums[i]] += 1
            if numCount[nums[i]] > 1:
                return True
        return False
            
        