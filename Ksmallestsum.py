class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
	rlist = [[]] * k
	lennums1 = len(nums1)
	lennums2 = len(nums2)
	index = [] * lennums1
	if lennums1 * lennums2 <= k:
		for i in range(lennums1):
			for j in range(lennums2):
				rlist.append((nums1[i],nums2[j])
				rlist = [rlist[i] for i in range(lennums1 * lennums2)) 
	else:
		for i in range(lennums1):
			#for j in range(lennums2):
				if nums1[i] + 
		
		


	
	return rlist


#http://bookshadow.com/weblog/2016/07/07/leetcode-find-k-pairs-with-smallest-sums/
		

