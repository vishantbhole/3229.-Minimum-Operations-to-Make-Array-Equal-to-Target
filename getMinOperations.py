#229.-Minimum-Operations-to-Make-Array-Equal-to-Target


class Solution(object):
    def getMinOperations(self, source, target):
         n = len(source)
        diff = [target[i] - source[i] for i in range(n)]

        ops = diff[0]
        for i in range(1, n):
            if diff[i] > diff[i-1]:
                ops += diff[i] - diff[i-1]

        return ops
