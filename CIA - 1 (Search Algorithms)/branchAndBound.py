import heapq
import graphLib

def branchAndBound(givenGraph, startNode, goalNode):
    queue = [(0, [startNode])]
    bestCost = float('inf')
    bestPath = None

    while queue:
        currentCost, currentPath = heapq.heappop(queue)
        currentNode = givenGraph.nodes[currentPath[-1]]

        if currentNode.nodeName == goalNode:
            if currentCost < bestCost:
                bestCost = currentCost
                bestPath = currentPath
            continue

        if currentCost >= bestCost:
            continue

        for neighbor, edgeCost in currentNode.neighbors:
            if neighbor.nodeName not in currentPath:
                newCost = currentCost + edgeCost
                newPath = currentPath + [neighbor.nodeName]
                heapq.heappush(queue, (newCost, newPath))

    return bestPath, bestCost

givenGraph = graphLib.Graph()

givenGraph.addNode("A")
givenGraph.addNode("B")
givenGraph.addNode("C")
givenGraph.addNode("D")
givenGraph.addNode("E")
givenGraph.addNode("S")
givenGraph.addNode("G")

givenGraph.addEdge("S", "A", 3)
givenGraph.addEdge("S", "D", 2)
givenGraph.addEdge("D", "E", 4)
givenGraph.addEdge("D", "B", 1)
givenGraph.addEdge("A", "B", 5)
givenGraph.addEdge("A", "C", 10)
givenGraph.addEdge("B", "C", 2)
givenGraph.addEdge("B", "E", 1)
givenGraph.addEdge("C", "G", 4)
givenGraph.addEdge("E", "G", 3)

path, cost = branchAndBound(givenGraph, 'S', 'G')

if path:
    print(f"Best Path found: {path}, Total Cost: {cost}")
else:
    print("No path found")
