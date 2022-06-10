class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix[0]), len(matrix)
        l, r = 0, m*n-1
        while(l<r):
            mid = l+(r-l)//2
            if(target>matrix[mid//m][mid%m]):
                l = mid + 1
            else:
                r = mid
        return matrix[l//m][l%m]==target