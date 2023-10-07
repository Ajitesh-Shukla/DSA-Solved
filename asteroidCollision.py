class Solution:
    def asteroidCollision(self, asteroids):
        new_astr=[]
        for i in range(len(asteroids)):
            toadd=True   # If we want to add this one or not
            while new_astr and new_astr[-1]>0 and asteroids[i]<0:  # Until collision happens
                if abs(asteroids[i])>abs(new_astr[-1]):
                    new_astr.pop()
                elif abs(asteroids[i])<abs(new_astr[-1]):
                    toadd=False
                    break
                else:
                    new_astr.pop()
                    toadd=False
                    break
            if toadd:
                new_astr.append(asteroids[i])
        return new_astr