def is_safe(board, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, len(board)), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True
def solve_n_queens_util(board, col):
    if col >= len(board[0]):
        return True
    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1
            if solve_n_queens_util(board, col + 1):
                return True
            board[i][col] = 0
    return False
def solve_n_queens(n, m):
    board = [[0 for _ in range(m)] for _ in range(n)]
    if not solve_n_queens_util(board, 0):
        return []
    return [i.index(1) for i in board]
solution_8x10 = solve_n_queens(8, 10)
print("Possible solution for 8x10 board:", solution_8x10)
def is_safe_with_obstacles(board, row, col, obstacles):
    if (row, col) in obstacles:
        return False
    return is_safe(board, row, col)
def solve_n_queens_with_obstacles(n, m, obstacles):
    board = [[0 for _ in range(m)] for _ in range(n)]
    for obs in obstacles:
        board[obs[0]][obs[1]] = -1  
    if not solve_n_queens_util(board, 0):
        return []
    return [i.index(1) for i in board if 1 in i]
obstacles_5x5 = [(1, 1), (2, 2)]
solution_5x5 = solve_n_queens_with_obstacles(5, 5, obstacles_5x5)
print("Possible solution for 5x5 board with obstacles:", solution_5x5)
def solve_n_queens_restricted(n, m, restricted):
    board = [[0 for _ in range(m)] for _ in range(n)]
    for pos in restricted:
        board[pos[0]][pos[1]] = -1 
    if not solve_n_queens_util(board, 0):
        return []
    return [i.index(1) for i in board if 1 in i]
restricted_6x6 = [(0, 0), (1, 1)]
solution_6x6 = solve_n_queens_restricted(6, 6, restricted_6x6)
print("Possible solution for 6x6 board with restricted positions:", solution_6x6)
