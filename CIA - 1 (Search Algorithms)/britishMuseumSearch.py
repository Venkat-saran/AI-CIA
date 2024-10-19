import graphLib

def britishMuseumSearch(graph, startNode, goalNode):
    def search(currentNode, visited, path, totalCost):
        path.append(currentNode.nodeName)
        if currentNode.nodeName == goalNode:
            return [(list(path), totalCost)]

        visited.add(currentNode.nodeName)
        allPaths = []
        for neighbor, cost in currentNode.neighbors:
            if neighbor.nodeName not in visited:
                allPaths += search(neighbor, visited.copy(), path.copy(), totalCost + cost)

        return allPaths

    visited = set()
    start = graph.nodes[startNode]
    return search(start, visited, [], 0)

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

allPaths = britishMuseumSearch(givenGraph, 'S', 'G')

for idVar, (path, cost) in enumerate(allPaths):
    print(f"Path {idVar + 1}: {path} with TOTAL COST: {cost}")