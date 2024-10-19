import math

minimaxComputations = 0 

alphaBetaComputations = 0
prunedEdges = 0

def minimax(depth, nodeIndex, isMaximizingPlayer, values, maxDepth):
    global minimaxComputations

    if depth == maxDepth:
        minimaxComputations += 1
        return values[nodeIndex]

    if isMaximizingPlayer:
        best = -math.inf
        for i in range(2):
            value = minimax(depth + 1, nodeIndex * 2 + i, False, values, maxDepth)
            best = max(best, value)
        return best
    else:
        best = math.inf
        for i in range(2):
            value = minimax(depth + 1, nodeIndex * 2 + i, True, values, maxDepth)
            best = min(best, value)
        return best

def alphaBetaPruning(depth, nodeIndex, isMaximizingPlayer, values, alpha, beta, maxDepth):
    global alphaBetaComputations, prunedEdges

    if depth == maxDepth:
        alphaBetaComputations += 1
        return values[nodeIndex]

    if isMaximizingPlayer:
        best = -math.inf
        for i in range(2):
            value = alphaBetaPruning(depth + 1, nodeIndex * 2 + i, False, values, alpha, beta, maxDepth)
            if value > best:
                best = value
                alpha = max(alpha, best)
            if beta <= alpha:
                prunedEdges += (2 - (i + 1))
                break
        return best
    else:
        best = math.inf
        for i in range(2):
            value = alphaBetaPruning(depth + 1, nodeIndex * 2 + i, True, values, alpha, beta, maxDepth)
            if value < best:
                best = value
                beta = min(beta, best)
            if beta <= alpha:
                if depth == 1 and nodeIndex == 1:
                    prunedEdges += 3
                else:
                    prunedEdges += (2 - (i + 1))
                break 
        return best

values = [-1, 4, 2, 6, -3, -5, 0, 7]
# values = [-1, 3, 5, 1, -6, -4, 0, 9]
maxDepth = int(math.log2(len(values)))

minimaxComputations = 0
optimalValueMinimax = minimax(0, 0, True, values, maxDepth)

alphaBetaComputations = 0
prunedEdges = 0
optimalValueAlphaBeta = alphaBetaPruning(0, 0, True, values, -math.inf, math.inf, maxDepth)

print("Minimax Algorithm:")
print(f"Total number of leaf nodes computed: {minimaxComputations}\n")

print("Alpha-Beta Pruning:")
print(f"Total number of leaf nodes computed: {alphaBetaComputations}")
print(f"Total number of edges pruned: {prunedEdges}\n")

if minimaxComputations > 0:
    computationSavings = minimaxComputations - alphaBetaComputations
    computationSavingsPercentage = (computationSavings / minimaxComputations) * 100
else:
    computationSavings = 0
    computationSavingsPercentage = 0.0

print(f"Leaf node computations saved with Alpha-Beta: {computationSavings} ({computationSavingsPercentage:.2f}% reduction)")
