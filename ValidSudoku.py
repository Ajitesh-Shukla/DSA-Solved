class Solution:
    def isValidSudoku(self, board):
        '''Simple way: check the three condtions using maps, always constant time since 9x9'''
        '''Can be implemented in one just two loops as well using 27 cells, but that is also easy, don't waste time'''
        # 1 check rowwise
        for rows in board:
            elem_check=set()
            for elem in rows:
                if elem!='.':
                    if elem in elem_check:
                        return False
                    elif int(elem)>9 or int(elem)<0:
                        return False
                    else:
                        elem_check.add(elem)
        # 2 Columnwise
        for j in range(9):
            elem_check=set()
            for i in range(9):
                elem=board[i][j]
                if elem!='.':
                    if elem in elem_check:
                        return False
                    elif int(elem)>9 or int(elem)<0:
                        return False
                    else:
                        elem_check.add(elem)
        # 3 cellwise
        for i in range(3):
            for j in range(3):
                submat=[rows[3*j:3*j+3] for rows in board[3*i:3*i+3]]
                elem_check=set()
                for k in range(3):
                    for l in range(3):
                        elem=submat[k][l]
                        if elem!='.':
                            if elem in elem_check:
                                return False
                            elif int(elem)>9 or int(elem)<0:
                                return False
                            else:
                                elem_check.add(elem)
        return True
