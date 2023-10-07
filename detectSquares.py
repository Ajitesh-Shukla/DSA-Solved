from collections import defaultdict
class DetectSquares:
    def __init__(self):
        self.ptsCount = defaultdict(int)
        self.pts = []

    def add(self, point) -> None:
        self.ptsCount[tuple(point)] += 1
        self.pts.append(point)

    def count(self, point) -> int:
        res = 0
        px, py = point
        for x, y in self.pts:
            if (abs(py - y) != abs(px - x)) or x == px or y == py:
                continue
            res += self.ptsCount[(x, py)] * self.ptsCount[(px, y)]
        return res

# class DetectSquares:

#     def __init__(self):
#         self.all_points={'X_based':{}, 'Y_based': {}, 'all_pts': {}}

#     def add(self, point) -> None:
#         if point[0] in self.all_points['X_based'].keys():
#             if point[1] in self.all_points['X_based'][point[0]].keys():
#                 self.all_points['X_based'][point[0]][point[1]]+=1
#             else:
#                 self.all_points['X_based'][point[0]][point[1]]=1
#         else:
#             self.all_points['X_based'][point[0]][point[1]]=1

#         if point[1] in self.all_points['Y_based'].keys():
#             if point[0] in self.all_points['Y_based'][point[1]].keys():
#                 self.all_points['Y_based'][point[1]][point[0]]+=1
#             else:
#                 self.all_points['Y_based'][point[1]][point[0]]=1
#         else:
#             self.all_points['Y_based'][point[1]][point[0]]=1
        
#         if (point[0], point[1]) in self.all_points['all_pts']:
#             self.all_points['all_pts'][(point[0], point[1])]+=1
#         else:
#             self.all_points['all_pts'][(point[0], point[1])]=1
            

#     def count(self, point) -> int:
#         ans=0
#         x, y=point[0], point[1]
#         all_y=self.all_points['X_based'][x]
#         all_x=self.all_points['Y_based'][y]

#         for y in all_y:
#             for x in all_x:
#                 numy=self.all_points['X_based'][x][y]
#                 numx=self.all_points['Y_based'][y][x]
#                 if (x,y) in self.all_points['all_pts'].keys():
#                     ans+=(self.all_points['all_pts'][(x,y)])*numy*numx
#         return ans