class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        latest_explosion=[]
        for i in asteroids:
            while latest_explosion and i<0 and latest_explosion[-1]>0:
                diff=i+latest_explosion[-1]
                if diff<0:
                    latest_explosion.pop()
                elif diff>0:
                    i=0
                else:
                    i=0
                    latest_explosion.pop()
            if i:
                latest_explosion.append(i)
        return latest_explosion


        

        