# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
	"""
	guessit(self,0,n)
    def guessit(self,x,y):
	ret = (y+x)/2
	if guess(ret) == 0:
		return ret
	elif guess(ret) == 1:
		return guessit(x,ret)
	else:
		return guessit(ret,y)
		     

