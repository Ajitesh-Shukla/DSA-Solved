class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        '''Key to this problem is the direction, we need to see which direction to go ltr or rtl'''
        pos_speed=list(zip(speed, position))
        pos_speed.sort(key= lambda x: x[1])   # sort based on position
        position=[elem[1] for elem in pos_speed][::-1]
        speed=[elem[0] for elem in pos_speed][::-1]

        stack=[]
        j=0
        while j<len(position):
            if stack:
                cur_t=(target-position[j])/(speed[j])
                if cur_t>stack[-1]:
                    stack.append(cur_t)
            else:
                stack.append(((target-position[j])/speed[j]))
            j+=1
        return len(stack)

        

