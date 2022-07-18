def decodeString(self, s):
    """
    :type s: str
    :rtype: str
    """
    cur_num = 0
    stack = []
    cur_str = ''
    for c in s:
        if c.isdigit():
            cur_num = int(c)+cur_num*10
        elif c == ']':
            num = stack.pop()
            prev_str = stack.pop()
            cur_str = prev_str+num*cur_str
        elif c == '[':
            stack.append(cur_str)
            stack.append(cur_num)
            cur_str = ''
            cur_num = 0
        else:
            cur_str += c
            
    return cur_str