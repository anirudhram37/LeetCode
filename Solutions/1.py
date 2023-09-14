class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for n in range(len(nums)):
            if nums[n] in hashmap:
                return [hashmap[nums[n]], n]
            else:
                hashmap[target - nums[n]] = n
