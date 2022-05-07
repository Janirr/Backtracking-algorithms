from graph import Graph


class Menu:

    def __init__(self, functions_array, texts_array, menu_title="MENU"):
        self.functions = functions_array
        self.texts = texts_array
        self.title = menu_title.upper()
        self.directed_graph = []
        self.undirected_graph = []

    def display(self):
        number = 0
        while number != len(self.functions) - 1:
            print("-- {} --".format(self.title))
            graph.connections()
            for i in range(len(self.functions)):
                print("{}: {}".format(i, self.texts[i]))
            try:
                number = int(input("Insert a number: "))
            except ValueError:
                print('Incorrect value')
            else:
                if len(self.functions) - 1 >= number >= 0:
                    if exec(self.functions[number]):
                        print(self.texts[number], exec(self.functions[number]))


list_of_edges = [[1, 2], [2, 3], [2, 5], [3, 1], [3, 4], [4, 6], [5, 3], [5, 4], [6, 1]]
graph = Graph(list_of_edges)
# 0 Inserting values
functions0 = ['graph.insertValues()', 'graph.deleteLastEdge()', 'graph.clearArray()', 'mainMenu.display()']
texts0 = ['Insert values', 'Delete last element', 'Clear', 'Go back']
menu0 = Menu(functions0, texts0, "Inserting values")
# 1 Get Data from File
functions1 = ['graph.readFile()', 'mainMenu.display()']
texts1 = ['Insert a file name', 'Go back']
menu1 = Menu(functions1, texts1, "Inserting a graph from the file")
# 2 Creating graphs / hamiltonian and euler cycles
functions2 = ['graph.createGraph()', 'graph.HamCycles()', 'graph.EulerCycles()', 'mainMenu.display()']
texts2 = ['Create a graph', 'Hamilton Cycle', 'Euler Cycle', 'Go back']
menu2 = Menu(functions2, texts2, "Creating graphs")
# 3 Create a random graph
functions3 = ['graph.randomGraph()', 'mainMenu.display()']
texts3 = ['Generate a graph', 'Go back']
menu3 = Menu(functions3, texts3, "Generate a random graph")
# Main menu
functions = ['menu0.display()', 'menu1.display()', 'menu2.display()', 'menu3.display()', 'exit()']
texts = ['Insert values', 'Get data from file', 'Create graphs / Operations on graphs', 'Create a random graph', 'Quit']
mainMenu = Menu(functions, texts, "Main menu")
mainMenu.display()
