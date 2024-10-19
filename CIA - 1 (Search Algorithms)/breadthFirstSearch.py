import graphLib
from collections import deque

def breadthFirstSearch(graph, startNode, goalNode):
    queue = deque([(graph.nodes[startNode], [startNode], 0)])
    visited = set()
    resultPaths = []
    goalLevel = None

    while queue:
        currentNode, currentPath, currentCost = queue.popleft()

        if currentNode.nodeName == goalNode:
            if goalLevel is None:
                goalLevel = len(currentPath) - 1
            if len(currentPath) - 1 == goalLevel:
                resultPaths.append((currentPath, currentCost))

        if goalLevel is not None and len(currentPath) - 1 > goalLevel:
            break

        if goalLevel is None or len(currentPath) - 1 < goalLevel:
            for neighbor, edgeCost in currentNode.neighbors:
                if neighbor.nodeName not in currentPath:
                    newPath = currentPath + [neighbor.nodeName]
                    newCost = currentCost + edgeCost
                    queue.append((neighbor, newPath, newCost))

        visited.add(currentNode.nodeName)

    return resultPaths

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

paths = breadthFirstSearch(givenGraph, 'S', 'G')

for path, cost in paths:
    print(f"Path: {path}, Total Cost: {cost}")