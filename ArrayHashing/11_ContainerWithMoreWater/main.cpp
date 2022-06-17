def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        r = len(height)-1
        max_now = 0
        while(l<r):
            temp = (r-l)*min(height[l],height[r])
            if temp>max_now: max_now = temp
            if height[l] < height[r]:
                l+=1;
            else:
                r-=1;
        return max_now