"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
    Given nums = [2, 7, 11, 15], target = 9,

    Because nums[0] + nums[1] = 2 + 7 = 9,
    return [0, 1].
"""
import time


def two_sum_pf(nums, target):
    if len(nums) <= 1:
        return False
    a = {}
    for i in range(len(nums)):
        if nums[i] in a:
            return [a[nums[i]], i]
        else:
            a[target - nums[i]] = i


def two_sum(nums, target):
    for i in range(0, len(nums)):
        for j in range(i+1, len(nums)):
            if (nums[i] + nums[j]) == target:
                return [i, j]


if __name__ == '__main__':
    t = time.time()
    print two_sum_pf([23, 4324, 341, 434, 33, 6, 15, -2, 7, 2], 0)
    print (time.time() - t) * 1000
