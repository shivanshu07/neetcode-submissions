class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(0, len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]
        seen = {}

        for i, num in enumerate(nums):
            compliment = target - nums[i]

            if compliment in seen:
                return [seen[compliment], i]

            seen[num] = i

        return []