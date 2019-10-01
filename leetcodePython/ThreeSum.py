'''
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    # 思路: 排序后遍历第一个数,剩下两个数在第一个数的右边首尾用双指针,三数之和小于0 则第二个数右移,三数之和大于0 则第三个数左移,任意一个数移动前后值相同可以直接跳过
    def threeSum(self, nums: [int]) -> [[int]]:
        nums.sort()
        res,i,length = [],0,len(nums)
        if length < 3:
            return res
        for i in range(length):
            if nums[i] > 0:
                break
            if i > 0 and nums[i-1] == nums[i]: # 第1个数移动前后相同,可以直接跳过
                continue
            l = i + 1
            r = length - 1
            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                if sum == 0:
                    res.append([nums[i],nums[l],nums[r]])
                    while l < r and nums[l] == nums[l+1]: # 第2个数移动前后相同,可以直接跳过
                        l += 1
                    while l < r and nums[r] == nums[r-1]: # 第3个数移动前后相同,可以直接跳过
                        r -= 1
                    l += 1
                    r -= 1
                elif sum < 0:
                    l += 1
                else:
                    r -= 1

        return res
