import matplotlib.pyplot as plt
import numpy as np
def plot_board(solution, N):
    board = np.zeros((N, N))
    for i in range(N):
        board[solution[i], i] = 1  
    fig, ax = plt.subplots()
    ax.imshow(board, cmap='binary')  
    ax.set_xticks(np.arange(N))
    ax.set_yticks(np.arange(N))
    for i in range(N):
        ax.text(i, solution[i], 'Q', ha='center', va='center', color='red', fontsize=20)
    plt.show()
def solve_nqueens(N):
    solutions = []
    solution = [-1] * N  
    def is_safe(row, col):
        for c in range(col):
            if solution[c] == row or \
               solution[c] - c == row - col or \
               solution[c] + c == row + col:
                return False
        return True
    def solve(col):
        if col == N:
            solutions.append(solution.copy()) 
            return
        for row in range(N):
            if is_safe(row, col):
                solution[col] = row  
                solve(col + 1)  
                solution[col] = -1  
    solve(0)
    return solutions
def visualize_nqueens_solutions(N):
    solutions = solve_nqueens(N)
    print(f"Number of solutions for N={N}: {len(solutions)}")
    for idx, solution in enumerate(solutions):
        print(f"Solution {idx + 1} for N={N}: {solution}")
        plot_board(solution, N)
print("4-Queens Visualization")
visualize_nqueens_solutions(4)
print("5-Queens Visualization")
visualize_nqueens_solutions(5)
