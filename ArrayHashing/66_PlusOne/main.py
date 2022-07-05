def plusOne(self, digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    if digits[-1] < 9:
        digits[-1] += 1
        return digits
    elif len(digits) == 1 and digits[0] == 9:
        return [1, 0]
    else:
        digits[-1] = 0
        digits[0:-1] = self.plusOne(digits[0:-1])
        return digits