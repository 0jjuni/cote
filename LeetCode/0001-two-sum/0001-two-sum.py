class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
        
            try:
                second = nums.index(target - nums[i])
            except:
                continue
            if i != second:
                return [i, second]
            