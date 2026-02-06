maze = [
    [0,0,1,0,0,0,1,0,0,0],
    [1,0,1,0,1,0,1,0,1,0],
    [1,0,0,0,1,0,0,0,1,0],
    [1,1,1,0,1,1,1,0,1,0],
    [0,0,0,0,0,0,1,0,0,0],
    [0,1,1,1,1,0,1,1,1,0],
    [0,1,0,0,0,0,0,0,1,0],
    [0,1,0,1,1,1,1,0,1,0],
    [0,0,0,1,0,0,0,0,0,0],
    [1,1,0,1,0,1,1,1,1,0],
]
# This is the main function to solve the maze
# input: maze
# return: route to the exit
def solve(maze):
    # initialize
    n, m = len(maze), len(maze[0])
    goal = (n-1, m-1)
    seen = set()
    path = []

    def dfs(r, c):
        # error check if it's out of the maze.
        if r < 0 or r >= n or c < 0 or c >= m: return False
        # check if it's wall, or already visited
        if maze[r][c] == 1 or (r, c) in seen: return False
        # check if it's goal
        if (r, c) == goal:
            return True

        seen.add((r, c)); 
        path.append((r, c))
        # search next block right/below/left/upper        
        if dfs(r, c+1):
            return True
        if dfs(r+1, c):
            return True
        if dfs(r, c-1):
            return True
        if dfs(r-1, c):
            return True

        path.pop()
        return False

    return path if dfs(0, 0) else None

ans_path = solve(maze)

# --- Print ---
def print_maze(maze, path):
    print("--- Print Path(*): ---")
    path = set(path) if path else set()
    for r in range(len(maze)):
        for c in range(len(maze[0])):
            if (r, c) in path:
                print("*", end=" ")
            elif maze[r][c] == 1:
                print("#", end=" ")
            else:
                print(".", end=" ")
        print()
    print("----------------------")
print_maze(maze, ans_path)
