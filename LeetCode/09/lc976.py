# LeetCode 976. Largest Perimeter Triangle `E`
# 1sk | 72% | 5'
# A~0v22

class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A.sort(reverse=True)
        for i in range(len(A)-2):
            if A[i] < A[i+1] + A[i+2]:
                return A[i]+A[i+1]+A[i+2]
        return 0
