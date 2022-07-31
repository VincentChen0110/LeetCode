    dic = [0]*(amount+1)
    
    def coinsub(amount):
        if amount < 0:
            return -1
        if amount == 0:
            return 0
        if dic[amount-1]!=0: return dic[amount-1]
        
        min_now = float('inf')
        for coin in coins:
            res = coinsub(amount-coin)
            if res>=0 and res<min_now:
                min_now = res+1
        
        dic[amount-1] = min_now
        if dic[amount-1] == float('inf'): return -1
        return dic[amount-1]
    
    if amount ==0 :return 0
    return coinsub(amount)