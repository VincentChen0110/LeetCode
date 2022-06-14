def evalRPN(tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for t in tokens:
            if t in '+-*/':
                b, a = stack.pop(), stack.pop()
                t = `int(eval(a+t+b+'.'))`
            stack += t,
        return int(stack[0])

tokens = ["4","13","5","/","+"]
print(evalRPN(tokens))