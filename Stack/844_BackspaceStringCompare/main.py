def backspaceCompare(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    stack_s = []
    stack_t = []
    
    for s_c in s:
        if s_c != '#' or s_c ==' ':stack_s.append(s_c)
        if s_c == '#' and stack_s: stack_s.pop()
    for t_c in t:
        if t_c != '#' or t_c ==' ':stack_t.append(t_c)
        if t_c == '#' and stack_t: stack_t.pop()
    return stack_s == stack_t