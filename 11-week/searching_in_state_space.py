from collections import deque

dirs = [(1, 2), (-1, 2), (1, -2), (-1, -2),
        (2, 1), (2, -1), (-2, 1), (-2, -1)]

def knight_path(start_x, start_y, end_x, end_y):
    visited = [[False] * 8 for i in range(8)]

    q = deque()
    q.append((start_x, start_y, 0))
    visited[start_x][start_y] = True

    while len(q) > 0:
        x, y, dist = q.popleft()
        if x == end_x and y == end_y:
            print(f"shortest distance is {dist}")
            return
        
        for dx, dy in dirs:
            x1, y1 = x + dx, y+dy
            if 0 <= x1 < 8 and 0 <= y1 < 8 and not visited[x1][y1]:
                q.append((x1, y1, dist+1))
                visited[x1][y1]
    print('unreachable')

knight_path(4, 4, 1, 5)