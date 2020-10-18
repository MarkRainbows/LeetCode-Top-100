# 给定 nums = [2, 7, 11, 15], target = 9
#
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]


class Solution:
    def twoSum(self, nums: list, target: int):
        for i in range(len(nums)):
            num = target - nums[i]
            if num in nums and nums.index(num) != i:
                return i, nums.index(num)


# for j in range(i + 1, len(nums)):
#     if nums[i] + nums[j] == target:
#         print(i, j)

