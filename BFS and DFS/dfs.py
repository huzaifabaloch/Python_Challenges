
class DFS():
    """
    To model depth first search algorithm.
    Uninformed search -> we have present knowledge but not for the entire
    domain. 
    Stack -> LIFO
    Deepest search.
    OUTPUT ---- > [0, 3, 2, 4, 1]
    """

    def __init__(self, vertex, neighbors):
        """To initialize the vertex and neigbors."""

        self.vertex = vertex
        self.neighbors = neighbors
        self.stack = list()
        self.visited = list()

    def adding_nodes(self):

        node = 0
        l = len(self.vertex)
        
        while l > 0:
            
            flag = False
            
            if self.stack == []:
                self.visited.append(self.vertex[0])
                self.stack.append(self.vertex[0])
                l -= 1
                continue


            node = self.stack[-1]

            for neighbor in self.neighbors:
                
                if node == neighbor[0]:
                    if node in self.stack:
                        self.stack.remove(node)

                    self.stack.append(neighbor[1])
                    flag = True


            if flag is False:
                    self.stack.pop()
                    
            self.visited.append(self.stack[-1])
            l -= 1
            
        print(self.visited)

# [0, 3, 2, 4, 1]
vertex = [0, 1, 2, 3, 4]
neighbors = [(0,1), (0,2), (0,3), (1,2), (2,4)]

dfs = DFS(vertex, neighbors)
dfs.adding_nodes()
