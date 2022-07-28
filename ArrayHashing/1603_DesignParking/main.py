def __init__(self, big, medium, small):
    """
    :type big: int
    :type medium: int
    :type small: int
    """
    self.parking = [big, medium, small]
    

def addCar(self, carType):
    """
    :type carType: int
    :rtype: bool
    """
    if self.parking[carType-1]:
        self.parking[carType-1]-=1
        return True
    else:
        return False