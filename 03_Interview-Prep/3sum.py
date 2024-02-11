class Solution:
    def twoSum(self, nums: List[int], i: int, possible):
        hashmap = set()
        j = i+1
        while j < len(nums):
            complement = - (nums[i] + nums[j])
            if complement in hashmap:
                possible.append([nums[i], nums[j], complement])
                while j+1 < len(nums) and nums[j] == nums[j+1]:
                    j+=1
            hashmap.add(nums[j])
            j+=1

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        possible = []
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i-1] != nums[i]:
                self.twoSum(nums, i, possible)
        return possible
