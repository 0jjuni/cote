class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_dic = dict()

        for i in range(len(nums)):
            try:
                if nums_dic[nums[i]]:
                    pass
            except:
                temp = nums[i]
                nums[i] = 1
                nums_dic[temp] = math.prod(nums)
                nums[i] = temp
            
        return [nums_dic[i] for i in nums]