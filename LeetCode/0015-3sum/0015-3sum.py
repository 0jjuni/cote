class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums)-2):
            left, right = i+1, len(nums)-1
            if i>0 and nums[i] == nums[i-1]:
                continue
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left +=1
                    right -=1
                elif sum > 0:
                    right -=1
                else:
                    left +=1
        return list({tuple(sorted(i)) for i in result})