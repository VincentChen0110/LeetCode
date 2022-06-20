dic = {"2":['a','b','c'],"3":['d','e','f'],"4":['g','h','i'],"5":['j','k','l'],"6":['m','n','o'],"7":['p','q','r','s'],"8":['t','u','v'],"9":['w','x','y','z']}
# This is NP hard problem, time complexity is O(N^4) since 4 chars most in 9 
## Iterative Solution
def letterCombinations(digits):
    all_combinations = [''] if digits else []
    for digit in digits:
        current_combinations = list()
        for letter in dic[digit]:
            for combination in all_combinations:
                current_combinations.append(combination + letter)
        all_combinations = current_combinations
    return all_combinations
## Backtracking Soluton
def letterCombinations(self, digits):
    if not digits: return []
    res = []
    self.dfs(digits,"",res)
    return res
    def dfs(self, digits, path, res):
        if not digits:
            res.append(path)
            return
        for char in dic[digits[0]]:
            self.dfs(digits[1:],path+char,res)

letterCombinations("23")