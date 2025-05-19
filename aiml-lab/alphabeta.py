MAX, MIN = 1000, -1000
def minimax(depth, nodeIndex, maximizingPlay, values, alpha, beta, d):
    if depth == d:
        return values[nodeIndex]
    if maximizingPlay:
        best = MIN
        for i in range(0,2):
            val = minimax(depth+1, nodeIndex*2+i, False, values, alpha, beta, d)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta<=alpha:
                break
        return best
    else:
        best = MAX
        for i in range(0,2):
            val = minimax(depth+1, nodeIndex*2+i, True, values, alpha, beta, d)
            best = min(best, val)
            beta = min(beta, best)
            if beta<=alpha:
                break
        return best
values = [3, 5, 6, 9, 1, 2, 0, -1]
print("Optimal value = ", minimax(0,0,True, values, MIN, MAX, 3))
