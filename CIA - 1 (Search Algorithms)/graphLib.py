class Node:
    def __init__(self, nodeName):
        self.nodeName = nodeName
        self.neighbors = []
        self.heuristic = 0  # For informed searches like A* and hill climbing

    def addNeighbor(self, neighbor, cost=1):
        self.neighbors.append((neighbor, cost))


class Graph:
    def __init__(self):
        self.nodes = {}

    def addNode(self, nodeName):
        if nodeName not in self.nodes:
            self.nodes[nodeName] = Node(nodeName)

    def addEdge(self, fromNode, toNode, cost=1):
        if fromNode in self.nodes and toNode in self.nodes:
            self.nodes[fromNode].addNeighbor(self.nodes[toNode], cost)

    def setHeuristic(self, nodeName, heuristic):
        if nodeName in self.nodes:
            self.nodes[nodeName].heuristic = heuristic