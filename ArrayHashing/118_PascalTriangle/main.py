def generate(numRows):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """
    # ans = [[1]]
    # if numRows==1:return ans
    # for i in range(1, numRows):
    #     temp = ans[i-1][:]
    #     temp.insert(0,0)
    #     temp.append(0)
    #     temp_ans = []
    #     for j in range(i+1):
    #         temp_ans.append(temp[j]+temp[j+1])
    #     ans.append(temp_ans)
    # return ans
    rows = [[1]]
    for r in range(1, numRows):
        rows.append([1] * (r+1))
        for c in range(1, r):
            rows[r][c] = rows[r-1][c] + rows[r-1][c-1]
    return rows 

print(generate(5))