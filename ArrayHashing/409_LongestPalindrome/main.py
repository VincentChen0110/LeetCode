def longestPalindrome(self, s):
    """
    :type s: str
    :rtype: int
    """
    # dic = {}
    # for char in s:
    #     dic[char] = dic.get(char, 0)+1
    # ans = 0
    # single = 0
    # for k, v in dic.items():
    #     if v%2==0: 
    #         ans+=v
    #     else:
    #         ans+=v-1
    #         single = 1
    # return ans+single
    hash = set()
    for c in s:
        if c not in hash:
            hash.add(c)
        else:
            hash.remove(c)
    # len(hash) is the number of the odd letters
    return len(s) - len(hash) + 1 if len(hash) > 0 else len(s)