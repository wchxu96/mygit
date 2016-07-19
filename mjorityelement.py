class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numsdict = {}
        for i in nums:
            if i not in numsdict:
                numsdict[i] = 1
            else:
                numsdict[i] = numsdict[i]+1
        return sorted(numsdict.items(),lambda x,y :cmp(x[1],y[1]),reverse=True)[0][0]
                
