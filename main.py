from graph import Graph
from menu import Menu

if __name__ == "__main__":
    list_of_edges = [[1, 2], [2, 3], [3, 4]]
    graph = Graph(list_of_edges)
    functions = ['menu0.display()', 'menu1.display()', 'menu2.display()', 'menu3.display()', 'exit()']
    texts = ['Insert values', 'Get data from file', 'Create graphs / Operations on graphs', 'Create a random graph', 'Quit']
    mainMenu = Menu(functions, texts, "Main menu")
    mainMenu.display()
