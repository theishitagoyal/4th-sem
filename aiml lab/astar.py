def print_state(state):
    for row in state:
        print(" ".join(map(str, row)))
    print()
def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j
def move(state, dir):
    i, j = find_blank(state)
    new = [row[:] for row in state] 
    if dir == "up" and i > 0:
        new[i][j], new[i-1][j] = new[i-1][j], new[i][j]
    elif dir == "down" and i < 2:
        new[i][j], new[i+1][j] = new[i+1][j], new[i][j]
    elif dir == "left" and j > 0:
        new[i][j], new[i][j-1] = new[i][j-1], new[i][j]
    elif dir == "right" and j < 2:
        new[i][j], new[i][j+1] = new[i][j+1], new[i][j]
    else:
        return None
    return new
def calc_heuristic(state, goal):
    h = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0 and state[i][j] != goal[i][j]: 
                h += 1
    return h
def a_star(initial, goal):
    OPEN = [(0 + calc_heuristic(initial, goal), 0, initial, [])]
    CLOSED = set()
    while OPEN:
        curr = min(OPEN, key=lambda x: x[0])
        OPEN.remove(curr)
        f, g, curr_state, path = curr
        print("Step: ", len(path))
        print_state(curr_state)
        if curr_state == goal:
            print("Solution found!")
            print("Steps to solution - ")
            for step in path:
                print(step)
            print("Total Steps required = ", len(path))
            return
        CLOSED.add(tuple(map(tuple, curr_state)))
        steps = ["up", "down", "left", "right"]
        for step in steps:
            succ = move(curr_state, step)
            if succ and tuple(map(tuple, succ)) not in CLOSED:
                h = calc_heuristic(succ, goal)
                g_succ = g + 1
                f_succ = g_succ + h
                OPEN.append((f_succ, g_succ, succ, path + [step]))
    print("Solution not found.")

initial = [[1, 2, 0], [8, 6, 3], [7, 5, 4]]
goal = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]
a_star(initial, goal)
