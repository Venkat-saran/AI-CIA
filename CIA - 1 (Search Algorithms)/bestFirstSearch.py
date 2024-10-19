import heapq
import graphLib

def bestFirstSearch(givenGraph, startNode, goalNode):
    queue = [(givenGraph.nodes[startNode].heuristic, 0, [startNode])]
    visited = set()

    while queue:
        _, currentCost, currentPath = heapq.heappop(queue)
        currentNode = givenGraph.nodes[currentPath[-1]]

        if currentNode.nodeName == goalNode:
            return currentPath, currentCost

        if currentNode.nodeName in visited:
            continue
        visited.add(currentNode.nodeName)

        for neighbor, edgeCost in currentNode.neighbors:
            if neighbor.nodeName not in visited:
                newPath = currentPath + [neighbor.nodeName]
                newCost = currentCost + edgeCost
                heapq.heappush(queue, (neighbor.heuristic, newCost, newPath))

    return None, None

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

givenGraph.setHeuristic("A", 9)
givenGraph.setHeuristic("B", 4)
givenGraph.setHeuristic("C", 2)
givenGraph.setHeuristic("D", 5)
givenGraph.setHeuristic("E", 3)
givenGraph.setHeuristic("S", 7)
givenGraph.setHeuristic("G", 0)

path, cost = bestFirstSearch(givenGraph, 'S', 'G')

if path:
    print(f"Path found: {path}, Total Cost: {cost}")
else:
    print("No path found")