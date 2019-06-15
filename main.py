from collections import defaultdict

#class Graph
class Graph:
    
    def __init__(self):
        self.graph = defaultdict(list)
        self.directed = False
        self.nodes = 0
        self.edges = 0

    def changeDirected(self):
        self.directed = True

    def setNodes(self,n):
        self.nodes = n
    
    def setEdges(self,n):
        self.edges = n

    def addEdge(self,u,v):
        if self.directed == False:
            self.graph[u].append(v)
            self.graph[v].append(u)
        else:
            self.graph[u].append(v)

    def isEdgeLessGraph(self):
        if edges == 0:
            return True
        else:
            return False

    def isCycleUtil(self, node, visited, parent):
        visited[node] = True
        print('p', node)
        for adj in self.graph[node]:
            if visited[adj] == False:
                print('c', adj)
                if self.isCycleUtil(adj, visited, node) == True:
                    return True
            elif parent != adj:
                return True
        return False

    def isCycle(self):
        visited = [False]*(self.nodes+1)
        for node in range(self.nodes):
            if visited[node+1] == False:
                if self.isCycleUtil(node+1, visited, -1) == True:
                    return True
        return False

    def isSimpleGraph(self):
        if self.isCycle() == True:
            return False
        else:
            return True
          
    def isRegularGraph(self,wantToPrint):
        isDegreeSame = True
        Degree = -1

        if self.directed == False:
            for i in range(2,nodes+1):
                if len(self.graph[i-1]) != len(self.graph[i]):
                    isDegreeSame = False
                    return Degree

            Degree = len(self.graph[1])
            if isDegreeSame == True and wantToPrint:
                print(Degree , '- Regular Graph')
        else:
            for i in range(2,nodes+1):
                if len(self.graph[i-1]) != len(self.graph[i]):
                    isDegreeSame = False
                    return Degree

            inDegrees = [0]*(self.nodes+1)
            for i in range(1,nodes+1):
                for j in range(0,len(self.graph[i])):
                    inDegrees[self.graph[i][j]] += 1

            for i in range(2,nodes+1):
                if inDegrees[i-1] != inDegrees[i]:
                    isDegreeSame = False
                    return Degree 

            inDegree = inDegrees[1]
            outDegree = len(self.graph[1])
            Degree = inDegree + outDegree      
                            
            if isDegreeSame == True  and wantToPrint:
                print(Degree, '- Regular Graph')
                print('InDegree : ', inDegree)
                print('OutDegree : ', outDegree)
        return Degree

    def isStronglyRegularGraph(self,wantToPrint):
        Degree = self.isRegularGraph(False)
        if Degree == -1:
            return False

        edgeSet = set()

        for i in range(1,nodes+1):
            for j in range(i+1,nodes+1):
                edgeSet.add((i,j))

        lemmda = -1

        for i in range(1,nodes+1):
            for j in self.graph[i]:
                if (i,j) in edgeSet:
                    edgeSet.remove((i,j))
                    Set1 = set()
                    Set2 = set()
                    Set1.clear()
                    Set2.clear()
                    for k in self.graph[i]:
                        Set1.add(k)
                    for k in self.graph[j]:
                        Set2.add(k)

                    Set1 = Set1.intersection(Set2)

                    if lemmda == -1:
                        lemmda = len(Set1)
                    elif lemmda != len(Set1):
                        return False

        MU = -1
        rightTerm = Degree * (Degree - lemmda - 1)
        leftTerm = (nodes - Degree - 1)

        if nodes == 1 or lemmda == -1 or leftTerm == 0:
            return False

        if rightTerm % leftTerm == 0:
            MU = rightTerm / leftTerm
            if wantToPrint:
                print('srg(Nodes = ',nodes,', Degree = ',Degree,', Lemmda = ',lemmda,', Mu = ',MU,')')
            return True
        else:
            return False



    def isCubicGraph(self):
        Degree = self.isRegularGraph(False)

        if Degree == 3:
            return True
        else:
            return False

    def BipartedDFS(self,node,visited,color):
        for u in self.graph[node]:
            if visited[u] == False:
                visited[u] = True
                color[u] = 1 - color[node]
                if self.BipartedDFS(u,visited,color)==False:
                    return False
            elif color[u]==color[node]:
                return False
        return True

    def isBipartedGraph(self):
        visited = [False]*(self.nodes+1)
        color = [False]*(self.nodes+1)
        visited[1] = True
        color[1] = 0
        if self.BipartedDFS(1,visited,color):
            return True
        else:
            return False

#Driver code
graph = Graph()

isUndirected = input('Is Graph Undirected (y/n)?: ')

if isUndirected == 'n':
    graph.changeDirected()

nodes = int(input('Enter total number of nodes: '))
edges = int(input('Enter total number of edges: '))
graph.setNodes(nodes)
graph.setEdges(edges)

for i in range(0,edges):
    u,v = input('Enter edge nodes u and v: ').split(" ")
    u = int(u)
    v = int(v)
    if u <= 0 or v <= 0 or u > nodes or v > nodes:
        print("Invalid")
        i = i-1
        continue     
    graph.addEdge(u,v)

print('isSimpleGraph : ' , graph.isSimpleGraph(),'\n')
print('isEdgeLessGraph : ' , graph.isEdgeLessGraph(),'\n')

if graph.isRegularGraph(True) == -1:
    print('isRegularGraph : False\n')
else:
    print('isRegularGraph : True\n')        

print('isStronglyRegularGraph : ' , graph.isStronglyRegularGraph(True),'\n')
print('isCubicGraph : ' , graph.isCubicGraph(),'\n')
print('isBipartedGraph : ',graph.isBipartedGraph(),'\n')

print("---------DONE------------")