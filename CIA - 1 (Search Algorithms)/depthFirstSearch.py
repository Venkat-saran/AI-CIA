import graphLib

def depthFirstSearch(graph, startNode, goalNode):
    def dfs(currentNode, currentPath, currentCost, visited):
        currentPath.append(currentNode.nodeName)

        visited.add(currentNode.nodeName)

        if currentNode.nodeName == goalNode:
            return currentPath, currentCost

        for neighbor, edgeCost in currentNode.neighbors:
            if neighbor.nodeName not in visited:
                result = dfs(neighbor, currentPath.copy(), currentCost + edgeCost, visited)
                if result:
                    return result

        return None

    visited = set()
    start = graph.nodes[startNode]
    result = dfs(start, [], 0, visited)
    return result

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

result = depthFirstSearch(givenGraph, 'S', 'G')

if result:
    path, cost = result
    print(f"Path found: {path}, Total Cost: {cost}")
else:
    print("No path found")