import operator

class Solution(object):
    cache = {} # cache for storing calculated equations 
    ops = {"+":operator.add, "-":operator.sub, "*":operator.mul}
    def diffWaysToCompute(self, input):
        ans = [] # ans for storing input's solutions
        if self.cache.has_key(input): return self.cache[input]
        for idx in xrange(len(input)):
            oper = input[idx]
            if self.ops.has_key(oper):
                left = self.diffWaysToCompute(input[:idx])
                right = self.diffWaysToCompute(input[idx+1:])
                
                for l in left:
                    for r in right:
                        ans.append(self.ops[oper](l, r))
                self.cache[input] = ans
        if not ans: # meet only digit
            ans.append(int(input))
        return ansclass Solution(object):
