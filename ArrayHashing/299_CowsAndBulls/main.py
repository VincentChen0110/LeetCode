def getHint(self, secret: str, guess: str) -> str:
    bulls = 0
    cows = 0
    dic_s = {}
    dic_g = {}
    for s, g in zip(secret, guess):
        if s==g:
            bulls+=1
        else:
            dic_s[s] = dic_s.get(s,0)+1
            dic_g[g] = dic_g.get(g,0)+1
    for k in dic_s:
        if k in dic_g:
            cows += min(dic_s[k], dic_g[k])
    
    return str(bulls)+"A"+str(cows)+"B"