class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        mums = [[x] for x in nums]
        l = len(nums)
        index = 0
        for i in range(1,l):
            maxi = i
            j = i-1
            while(j >= 0):
                if nums[i]% nums[j] == 0 and len(mums[i])+1 > len(mums[maxi]):
                    maxindex = j
                if maxi!=i:
                    mums[maxi] = mums[i] + mums
                else:
                    j = j - 1
        return sorted(max(mums[i] for i in range(l),key=len))


def largestDivisibleSubset(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    l = len(nums)
    if l <= 1:
        return nums
    nums = sorted(nums)
    mem = [[x] for x in nums]
    index = 0
    
    for i in range(1,l):
        maxi = i
        for j in range(i):
            if nums[i]%nums[j] == 0 and len(mem[j]) + 1 > len(mem[maxi]):
                maxi = j
        if maxi != i:
            mem[i] = mem[maxi]+mem[i]
            
        if len(mem[i]) > len(mem[index]):
            index = i

    return mem[index]



#http://www.lexev.org/en/2015/base-python-tips-tricks/
