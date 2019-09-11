
class BFS():
    """
    To model a breadth first search.
    Uninformed search technique -> no cost knowlege between nodes.
    FIFO (queue)
    shallowest node
    """

    def __init__(self, vertex, neighbors):
        """To initialize the attributes."""

        # To store all the vertex(nodes)
        self.vertex = vertex
        
        # To store the edges means what which vertex is connected to which.
        self.neighbors = neighbors

        # BFS is a FIFO structure, so the first node from tail
        # and removed from head.
        self.queue = list()

        # To store those all the nodes after successfully parsed.
        self.visited = list()

    def adding_nodes(self):
        """
        Here we simply iterate through each node or vertex and add
        to the queue. Then we see who are neighbors of it and add them
        too in the queue, then we remove the first element that entered
        from head of queue and repeat the same process for next vertex
        like 1, we check whether it is in the queue or not if yes, we
        donot insert it again and then we check it neighbors and add them
        too to the queue and so on.
        Finally whenever an node is removed from queue it is added to the
        visited list.
        """
        
        for node in self.vertex:
            i = 0
            if node not in self.queue:
                self.queue.append(node)

            for neigbor in self.neighbors:
                if node == neigbor[0]:
                    if neigbor[-1] not in self.queue:
                        self.queue.append(neigbor[-1])
  
            self.visited.append(self.queue.pop(i))

        return self.visited


vertex = [0, 1, 2, 3, 4]
neighbors = [(0,1), (0,2), (0,3), (1,2), (2,4)]

bfs = BFS(vertex, neighbors)
print(bfs.adding_nodes())
