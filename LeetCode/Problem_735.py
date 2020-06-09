# Problem 735 : Asteroid Collision

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            if asteroid > 0:
                stack.append(asteroid)
            else:
                temp = True
                while len(stack) > 0:
                    top = stack.pop()
                    if top < 0:
                        stack.append(top)
                        stack.append(asteroid)
                        break
                    elif abs(top) > abs(asteroid):
                        stack.append(top)
                        break
                    elif abs(top) == abs(asteroid):
                        temp = False
                        break
                    else:
                        pass
                if len(stack) == 0 and temp:
                    stack.append(asteroid)
        return stack
