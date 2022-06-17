
n = 3
### n = 2: ["(())","()()"]

## Solution 1: Iterative method
def generateParenthesis(n):
    res = []
    s = [("(",1,0)]
    while s:
        x, l, r = s.pop()
        if l<r or l>n or r >n:
            continue
        if l==n and r==n:
            res.append(x)
        s.append((x+"(",l+1,r))
        s.append((x+")",l,r+1))

    print(res)

## Solution 2: Dynamic Programming
def generateParenthesis(n):
    def generate(p,left, right,parens = []):
        if left: generate(p+"(",left-1,right)
        if right>left: generate(p+")",left,right-1)
        if not right: parens+=p,
        return parens

    generate("", n, n)
print(generateParenthesis(n))