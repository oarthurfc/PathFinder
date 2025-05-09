import heapq

# Representa um nó no labirinto
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])  # Distância de Manhattan

def a_star_search(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    open_set = []
    heapq.heappush(open_set, (0, start))

    came_from = {}  # Para reconstruir o caminho
    g_score = {start: 0}

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == end:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path

        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            neighbor = (current[0] + dx, current[1] + dy)
            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols:
                if maze[neighbor[0]][neighbor[1]] != 1:
                    tentative_g_score = g_score[current] + 1
                    if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                        came_from[neighbor] = current
                        g_score[neighbor] = tentative_g_score
                        f_score = tentative_g_score + heuristic(neighbor, end)
                        heapq.heappush(open_set, (f_score, neighbor))

    return None

def print_maze_with_path(maze, path):
    visual = [['S' if (i, j) == path[0] else 'E' if (i, j) == path[-1] else '1' if maze[i][j] == 1 else '0' for j in range(len(maze[0]))] for i in range(len(maze))]
    for i, j in path[1:-1]:
        visual[i][j] = '*'
    for row in visual:
        print(' '.join(row))

if __name__ == "__main__":
    maze = [
        ['S', 0, 1, 0, 0],
        [0, 0, 1, 0, 1],
        [1, 0, 1, 0, 0],
        [1, 0, 0, 'E', 1]
    ]

    # Converte S, E e 0 para valores padronizados
    start = end = None
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 'S':
                start = (i, j)
                maze[i][j] = 0
            elif maze[i][j] == 'E':
                end = (i, j)
                maze[i][j] = 0

    if not start or not end:
        print("Labirinto inválido: ponto inicial (S) ou final (E) não encontrado.")
    else:
        path = a_star_search(maze, start, end)
        if path:
            print("Caminho encontrado:", path)
            print("\nLabirinto com caminho destacado:")
            print_maze_with_path(maze, path)
        else:
            print("Sem solução.")
