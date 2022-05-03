import random
import time


class Graph:

    def __init__(self, edges_array):
        self.edges = edges_array
        self.undirected_graph = []
        self.directed_graph = []
        self.hasHamCycle = False

    def display(self):
        print(*self.edges)

    def insertValues(self):
        leave = False
        while not leave:
            print("Connections:", *self.edges)
            print("To go back, please press enter without any values\n")
            edge = []
            try:
                edge = list(map(int, input("Pass 2 numbers separated by space: ").split()))
                if len(edge) == 2:
                    self.edges.append(edge)
            except ValueError:
                print('Incorrect value')
            if not edge:
                leave = True
                print("\n")

    def connections(self):
        print("Connections:", *self.edges)

    def createGraph(self):
        if len(self.edges) > 0:
            vertexes = []
            if len(self.edges) > 0:
                for i in range(len(self.edges)):
                    vertexes.append(self.edges[i][0])
                    vertexes.append(self.edges[i][1])
                vertexes = set(vertexes)
                n = len(vertexes)
                self.undirected_graph = [[0] * n for i in range(n)]
                self.directed_graph = [[] * n for i in range(n)]
                for i in range(len(self.edges)):
                    x = self.edges[i][0] - 1
                    y = self.edges[i][1] - 1
                    self.undirected_graph[x][y] = 1
                    self.undirected_graph[y][x] = 1
                    self.directed_graph[x].append(y + 1)
                print("\n-- UNDIRECTED GRAPH --")
                print(*self.undirected_graph, sep="\n")
                print("\n-- DIRECTED GRAPH --")
                for j in range(n):
                    print(j + 1, *self.directed_graph[j], sep="=>")
            print("\nPress ENTER to continue")
            option = ' '
            while option != '':
                option = input()

    def randomGraph(self):
        n = 0
        s = 0
        try:
            n = int(input("Enter number of vertexes: "))
        except ValueError:
            print('Incorrect value')
        try:
            s = int(input("Enter the density of the graph [1-100]: "))
        except ValueError:
            print('Incorrect value')
        edges_list = []
        max_edges = (n * (n - 1))
        for i in range(n):
            for j in range(n):
                if i != j:
                    edge = [i + 1, j + 1]
                    edges_list.append(edge)
        random_list_directed = random.sample(range(1, max_edges), int(abs(s - 100) / 100 * max_edges))
        random_list_directed.sort(reverse=True)
        for i in random_list_directed:
            edges_list.pop(i)
        self.edges = edges_list
        # end = time.time()
        # print("Time:", end - start)

    def deleteLastEdge(self):
        if len(self.edges) > 0:
            print("Deleted element: ", self.edges[-1])
            self.edges.pop()

    def clearArray(self):
        self.edges = []
        self.undirected_graph = []
        self.directed_graph = []
        self.hasHamCycle = False

    def isSafe(self, v, path, pos):
        if self.undirected_graph[path[pos - 1]][v] == 0:
            return False
        for i in range(pos):
            if path[i] == v:
                return False
        return True

    def hamCycle(self):
        if len(self.undirected_graph) > 0:
            path = [0]  # Starting from first value
            visited = [False] * (len(self.undirected_graph))
            for i in range(len(visited)):
                visited[i] = False
            visited[0] = True
            self.findHamCycle(1, path, visited)
            if not self.hasHamCycle:
                print("Graf wejściowy nie zawiera cyklu.")
                return

    def findHamCycle(self, pos, path, visited):
        if not self.hasHamCycle:
            if pos == len(self.undirected_graph):  # Found a cycle
                if self.undirected_graph[path[-1]][path[0]] != 0:
                    self.hasHamCycle = True
                    path.append(0)
                    printable_path = []  # Values from 1 to n+1
                    for i in range(len(path) - 1):
                        printable_path.append(path[i] + 1)
                    print("Hamiltonian cycle:", printable_path)
                    path.pop()
                return
            for v in range(len(self.undirected_graph)):
                if self.isSafe(v, path, pos) and not visited[v]:
                    path.append(v)
                    visited[v] = True
                    self.findHamCycle(pos + 1, path, visited)
                    visited[v] = False
                    path.pop()

    def readFile(self):
        print("Press ENTER to go back")
        option = ' '
        while option != '':
            option = input("Enter file name: ")
            try:
                f = open(option)
                self.edges = []
                n, k = map(int, f.readline().split())
                for i in range(k):
                    connection = list(map(int, f.readline().split()))
                    self.edges.append(connection)
                print("Data has been imported correctly\n")
                option = ''
                f.close()
            except IOError:
                print("File cannot be read\n")
