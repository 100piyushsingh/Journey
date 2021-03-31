class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        for i in range(len(nums)-2):
            if nums[i] > 0:
                break
            if i == 0 or (i > 0 and nums[i] != nums[i-1]):
                sum1 = 0 - nums[i]
                low = i+1
                high = len(nums) - 1
                while low < high:
                    if (nums[low] + nums[high] == sum1):
                        res.append([nums[i],nums[low],nums[high]])
                        while low < high and nums[low] == nums[low+1]:
                            low += 1
                        while low < high and nums[high] == nums[high-1]:
                            high -= 1
                        low += 1
                        high -= 1
                    elif (nums[low] + nums[high] < sum1):
                        low += 1
                    else:
                        high -= 1
        return res
