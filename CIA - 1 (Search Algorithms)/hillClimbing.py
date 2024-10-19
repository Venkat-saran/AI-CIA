import graphLib

def hillClimbing(graph, startNode, goalNode):
    currentNode = graph.nodes[startNode]
    currentPath = [currentNode.nodeName]
    currentCost = 0

    while currentNode.nodeName != goalNode:
        neighbors = currentNode.neighbors
        if not neighbors:
            print("No more neighbors to explore. Stuck in local optima.")
            return currentPath, currentCost

        nextNode, edgeCost = min(neighbors, key=lambda x: x[0].heuristic)

        if nextNode.heuristic >= currentNode.heuristic:
            print("Reached local optima, cannot find a better neighbor.")
            return currentPath, currentCost

        currentNode = nextNode
        currentCost += edgeCost
        currentPath.append(currentNode.nodeName)

    return currentPath, currentCost

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

path, cost = hillClimbing(givenGraph, 'S', 'G')

print(f"Path found: {path}, Total Cost: {cost}")
