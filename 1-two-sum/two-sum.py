class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}

        for i in range(len(nums)):
            req = target - nums[i]
            if req in dic:
                return [dic[req], i]
            else:
                dic[nums[i]] = i