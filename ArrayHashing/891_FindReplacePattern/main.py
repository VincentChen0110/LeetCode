def findAndReplacePattern(self, words, pattern):
    """
    :type words: List[str]
    :type pattern: str
    :rtype: List[str]
    """
    ans = []
    
    for word in words:
        word_dic = {}
        flag = True
        for w, p in zip(word, pattern):
            if w not in word_dic:
                if p in word_dic.values():
                    flag = False
                word_dic[w] = p
            else:
                if word_dic[w] != p:
                    flag = False
        if flag:
            ans.append(word)
    return ans