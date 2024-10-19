# CIA 2: Alpha-Beta Pruning and Minimax Algorithm

This folder contains the implementation of both the **Minimax** algorithm and its optimized version, **Alpha-Beta Pruning**.

## Algorithms Implemented

### 1. **Minimax Algorithm**
   - The **Minimax** algorithm is used in decision-making processes, particularly in adversarial environments (such as two-player games).
   - It explores all possible outcomes of moves for both players (Maximizer and Minimizer) without pruning any branches.
   - **Time complexity**: O(b^d), where **b** is the branching factor and **d** is the depth of the game tree.

### 2. **Alpha-Beta Pruning**
   - This is an optimization over **Minimax**, which "prunes" branches that are guaranteed not to affect the final decision.
   - It keeps track of two values: **alpha** (the best value the maximizer can guarantee) and **beta** (the best value the minimizer can guarantee).
   - If a branch can’t improve the outcome for either player, it is pruned, reducing the number of computations.
   - **Time complexity**: O(b^(d/2)) in the best case, making it more efficient than Minimax.

## Input

The algorithms operate on a fixed binary tree where the values at the leaf nodes represent the possible outcomes of a game.
```python
values = [-1, 4, 2, 6, -3, -5, 0, 7]