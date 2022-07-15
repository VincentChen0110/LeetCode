def dailyTemperatures(self, temperatures):
    """
    :type temperatures: List[int]
    :rtype: List[int]
    """
    # ans = []
    # for i, temp in enumerate(temperatures[:-1]):
    #     for j, temps in enumerate(temperatures[i+1:]):
    #         if (temps-temp) > 0:
    #             ans.append(j+1)
    #             break
    #         if j == len(temperatures) - 2 - i:
    #             ans.append(0)
    # ans.append(0)
    # return ans
    stack = []
    ans = [0]*len(temperatures)
    for i, temp in enumerate(temperatures):
        while stack and stack[-1][1] < temp:
            index, value = stack.pop()
            ans[index] = i-index  
        stack.append([i,temp])
    return ans