all_paths=[]
mat=[[1, 0, 0, 0],
    [1, 1, 0, 1],
    [1, 1, 0, 0],
    [0, 1, 1, 1]]

def getPath(i, j, maze, path, all_paths):
    # Base
    if i==len(maze)-1 and j==len(maze[0])-1:
        path.append((i, j))
        all_paths.append(path.copy())
        path.pop(-1)
        return True
    
    # Compute
    if i>=len(maze) or j>=len(maze[0]):
        return False
    elif maze[i][j]==0:
        return False

    path.append((i, j))
    p1=getPath(i+1, j, maze, path, all_paths)
    p2=getPath(i, j+1, maze, path, all_paths)
    path.pop(-1)   # Checked all paths from (i, j), thus back to previous now
    if p1 or p2:
        return True

ans=getPath(0, 0, mat, [], all_paths)


