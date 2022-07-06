def findRestaurant(list1, list2):
    """
    :type list1: List[str]
    :type list2: List[str]
    :rtype: List[str]
    """
    # ans = {}
    # final_ans = []
    # for i in range(len(list1)):
    #     for j in range(len(list2)):
    #         if list1[i]==list2[j]:
    #             if (i+j) not in ans:
    #                 ans[i+j] = [list1[i]]
    #             else:
    #                 ans[i+j].append(list1[i])

    
    # sortedkeys = sorted(ans.keys())
    # return ans[sortedkeys[0]]

    dic1 = {res:i for i, res in enumerate(list1)}
    dic2 = {res:dic1[res]+i for i, res in enumerate(list2) if res in dic1}
    
    res = []
    MIN = float('inf')
    for key, val in dic2.items():
        if val < MIN:
            res = [key]
            MIN = val
        elif val == MIN:
            res.append(key)
            
    return res

list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
list2 = ["KFC","Burger King","Tapioca Express","Shogun"]

print(findRestaurant(list1, list2))