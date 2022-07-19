def simplifyPath(self, path):
    """
    :type path: str
    :rtype: str
    """
    stack = []
    for elem in path.split("/"):
        if stack and elem == "..":
            stack.pop()
        elif elem not in [".", "", ".."]:
            stack.append(elem)
            
    return "/" + "/".join(stack)