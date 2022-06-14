def evalRPN(tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        if not tokens: return 0
        stack = []
        for item in tokens:
            if item in "+-*/":
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(str(int(eval(val2+item+val1))))
            else:
                stack.append(item)
            
        return int(stack.pop())

tokens = ["4","13","5","/","+"]
print(evalRPN(tokens))