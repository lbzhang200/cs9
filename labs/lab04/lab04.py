from Stack import Stack 

def solveMaze(maze, startX, startY):
    stack = Stack()
    steps = 1 

    maze[startX][startY] = steps 

    stack.push([startX, startY])

    while not stack.isEmpty():
        current = stack.peep()
        x = current[0]
        y = current[1] 

        neighbors = [[x-1, y], [x+1, y], [x, y-1], [x, y+1]]

        moved = False 
        for pos in neighbors:
            nx = pos[0] 
            ny = pos[1]

            if maze[nx][ny] == 'G':
                return True 
            if maze[nx][ny] == ' ':
                steps += 1
                maze[nx][ny] = steps 
                stack.push([nx, ny])
                moved = True 
                break

        if not moved:
            stack.pop()
    return False 