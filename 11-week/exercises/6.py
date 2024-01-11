
from collections import deque

maze = [
    ['#','#','#','#','#','#','#','#'],
    ['#', ' ', '#', ' ', ' ',  '#', ' ', '#'],
    ['#', ' ', '#', ' ', '#', ' ',  ' ', '#'],
    ['#', ' ', ' ', ' ', '#', ' ', '#', '#'],
    ['#', '#', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', '#', '#', '#', '#', '#', '#', '#']
]


def print_maze():
    for row in maze:
        for item in row:
            print(item, end="")
        print()

def get_empty_squares():
    empty_squares = []
    
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == ' ':
                empty_squares.append((i, j))
    
    return empty_squares

dirs = [ 
    (1, 0), (-1, 0), (0, 1), (0, -1), 
    (1, 1), (-1, 1), (1, -1), (-1, -1)
]

def find_path(start_x, start_y, end_x, end_y):
    visited = [[False] * len(i) for i in maze]

    q = deque()
    q.append( (start_x, start_y, 0) )
    visited[start_x][start_y] = True

    while len(q) > 0:
        x, y, dist = q.popleft()

        if x == end_x and y == end_y: return True

        for dx, dy in dirs:
            x1, y1 = x + dx, y + dy
            if 0 <= x1 < 8 and 0 <= y1 < 8 and maze[x1][y1] != '#' and not visited[x1][y1]:
                q.append( (x1, y1, dist + 1) )
                visited[x1][y1] = True
    
    return False

def is_connected(maze):
    empty_squares = get_empty_squares()
    visited = [[False] * len(i) for i in maze]
    for square in empty_squares:
        for square2 in empty_squares:
            if square != square2 and not visited[square2[0]][square2[1]]:
                if not find_path(square[0], square[1], square2[0], square2[1]):
                    print('not connected')
                    return
                visited[square2[0]][square2[1]] = True
    print('this maze is connected')

print_maze()
print()
is_connected(maze)