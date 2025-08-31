#229.-Minimum-Operations-to-Make-Array-Equal-to-Target


class Solution(object):
    def getMinOperations(self, source, target):
         n = len(source)
        diff = [target[i] - source[i] for i in range(n)]

         # impossible case
        if any(d < 0 for d in diff):
            return -1
            
        ops = diff[0]
        for i in range(1, n):
            if diff[i] > diff[i-1]:
                ops += diff[i] - diff[i-1]

        return ops

if __name__ == "__main__":
    sol = Solution()
    source = [1, 2, 2]
    target = [2, 2, 3]
    result = sol.getMinOperations(source,target)
    print("Output is:", result)


# Complexity:
# Time: O(n)
# Space: O(n) (can be reduced to O(1) if we compute on the fly).
