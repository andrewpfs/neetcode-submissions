class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:


        for ind in range(0,len(nums)-1): 
            for future in range(ind+1, len(nums)):
                if(nums[ind] + nums[future] == target):
                    return [ind, future]

        return [0]