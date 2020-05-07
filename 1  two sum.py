

# Documentation 两数之和

# Given nums = [2, 7, 11, 15], target = 9,
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].


list1 = [1, 4, 6, 8, 10, 11]
target_num = 18

# solution 1  暴力解决法

'''
class Solution:
    def two_sum(self, nums: list, target: int):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return print(nums[i], nums[j])


sou = Solution()
sou.two_sum(list1, target_num)

'''


# Soulation 2  排除法

'''
class Solution:
    def two_sum1(self, nums: list, target: int):
        for i in range(len(nums)):
            one_num = target - nums[i]
            if one_num in list1:
                return print(nums[i], one_num)


sou1 = Solution()
sou1.two_sum1(list1, target_num)

'''

