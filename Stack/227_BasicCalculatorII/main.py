def calculate(self, s):
    """
    :type s: str
    :rtype: int
    """
    num = 0
    stack = []
    presign = '+'
    
    for i in s+'+':
        if i.isdigit():
            num = num*10+int(i)
        elif i in "+-*/":
            if presign == "+":
                stack.append(num)
            if presign == "-":
                stack.append(-num)
            if presign == "*":
                stack.append(stack.pop()*num)
            if presign == '/':
                stack.append(int(stack.pop()/float(num)))
            presign = i
            num = 0
    return sum(stack)
