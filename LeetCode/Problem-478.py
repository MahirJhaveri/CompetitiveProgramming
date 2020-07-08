# Problem 478: Generate random points in a circle

class Solution(object):
    
    import random

    def __init__(self, radius, x_center, y_center):
        """
        :type radius: float
        :type x_center: float
        :type y_center: float
        """
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center
        
        

    def randPoint(self):
        while True:
            x,y = random.uniform(self.x_center-self.radius, self.x_center+self.radius), random.uniform(self.y_center-self.radius, self.y_center+self.radius)
            if (x-self.x_center)**2 + (y-self.y_center)**2 <= self.radius**2:
                return [x,y]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()
