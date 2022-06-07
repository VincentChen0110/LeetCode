class Solution:
    def isValid(self, s: str) -> bool:
        stack = ['X']
        paran_dict = {")":"(","]":"[","}":"{"}
        for char in s:
            if char in paran_dict.keys():
                if stack.pop() != paran_dict[char]: 
                    return False
            else:
                stack.append(char)
        return len(stack)==1

