

# Documentation 两数之和

# Given nums = [2, 7, 11, 15], target = 9,
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].


list1 = [1, 4, 6, 8, 10, 11]
target_num = 18


class Solution:

    # 暴力破解  内存消耗过多  用时过长
    def twoSum(self, nums: list, target: int):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return print(nums[i], nums[j])

    # 排除法  内存消耗一般  用时速度较快
    def twoSum1(self, nums: list, target: int):
        for i in range(len(nums)):
            num = target - nums[i]
            if num in nums and nums.index(num) != i:
                return i, nums.index(num)









