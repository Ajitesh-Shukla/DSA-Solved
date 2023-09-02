class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        '''Search all locations for the first element, then do bfs recursively'''
        dir=[[-1, 0], [1, 0], [0, -1], [0, 1]]
        vis=set()  # To not interfare with the previous character
        def search(i, pos):  # i is the position in the word
            # print(vis, pos, i, len(word), word[-1])
            if i==len(word)-1 and board[pos[0]][pos[1]]==word[-1]:   # Reached the end of word
                return True
            if i>=len(word):
                return False
            
            for dirn in dir:
                x, y=pos[0]+dirn[0], pos[1]+dirn[1]
                if x>=0 and y>=0 and x<len(board) and y<len(board[0]) \
                    and board[x][y]==word[i+1] and (x, y) not in vis:
                    vis.add((x, y))
                    res=search(i+1, (x, y))
                    if res:
                        return True
                    vis.remove((x,y))
            return False
        
        all_start=[]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==word[0]:
                    all_start.append((i, j))

        for elem in all_start:
            vis.add((elem))
            if search(0, elem):
                return True
            vis.remove((elem))
        return False
                    


