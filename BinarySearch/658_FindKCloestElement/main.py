def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
    l, r = 0, len(arr)-k
    ### Consider window size k, starting l from 0
    ### [1,2,3,4,5], left-right
    # while(l<r):
    #     m = l+(r-l)//2
    #     ## Case1: if target on left hand side, update right pointer
    #     if arr[m] >= x: r = m 
    #     ## Case2: if right pointer is still smaller than x, update left pointer
    #     elif arr[m+k] < x: l = m+1 
    #     ## Case3 if arr[m]<x<arr[m+k]
    #     ## Case3.1 if arr[m] is closer to x than arr[m+k], arr[m+k] is bad choice, search left
    #     elif x - arr[m] > arr[m + k] - x: l = m + 1
    #     ## Case3.2 Vice Versa, search right
    #     else: r = m
    # return arr[l : l + k]
    while(l<r):
        m = l+(r-l)//2
        if x-arr[m]>arr[m+k]-x:
            l = m+1
        else:
            r = m
    return arr[l:l+k]
arr = [1,2,3,4,5]
k = 4
x = 3
print(findClosestElements(arr,k,x))