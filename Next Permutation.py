class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        reverse_nums = nums[:]
        sort_nums = nums[:]
        reverse_nums.reverse()
        sort_nums.sort()
        
        if n==1 or n==2:
            nums.reverse()
            return nums
        if reverse_nums == sort_nums :
            return reverse_nums
        
        for i in range(n-1,0,-1):
            if nums[i] > nums[i-1]:
                for j in range(n-1,i-1,-1):
                    if nums[j] > nums[i-1]:
                        nums[j],nums[i-1] = nums[i-1],nums[j]
                        break
                    else:
                        continue
                new1_nums = nums[i:]
                new1_nums.reverse()
                nums = nums[0:i]
                nums.extend(new1_nums)
                return nums
            else:
                continue
         
