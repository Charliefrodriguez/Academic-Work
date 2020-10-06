"""We are going to build our graph node class here"""

#We are going to experiment a bit with classes and nodes
class GraphNode:
    """This is my first experiment with a class"""
    def __init__(self, terrain, path_diff, name):
        self.terrain = terrain #terrain difficulty
        self.path_diff = path_diff # edge weigh between two nodes
        self.name = name #this is going to be represent by the index in which the node is created
        self.after = None

    def get_ter(self):
        """This is a getter function for terrain"""
        return self.terrain

    def get_path(self):
        """This is a getter function for path difficulty"""
        return self.path_diff

    def get_name(self):
        """This is a getter function for name of the node"""
        return self.name

class LinkedList:
    """Here we are going to build out linked list """
    def __init__(self, terrain, path_diff, name):

        GraphNode.__init__(self, terrain, path_diff, name)
        self.head = GraphNode(terrain, path_diff, name)

    def insert(self, terrain, path_diff, name):
        """This method will insert nodes into our linked list """
        ptr = self.head
        while ptr.after is not None:
            ptr = ptr.after

        if ptr.after is None:
            ptr.after = GraphNode(terrain, path_diff, name)

    def print_list(self):
        """ Prints out the members of the linked list """
        ptr = self.head
        while ptr is not None:
            print("name " + str(ptr.name) + " " + "terrain " + str(ptr.terrain))
            ptr = ptr.after

class AdjList:
    """Here we are going to build the adjaceny linked list """
    def __init__(self, x_dim, y_dim):
        prod = x_dim * y_dim 
        self.prod = prod
        self.lst = [0] * (prod)
        for i in range(prod):
            self.lst[i] = LinkedList(0, 1, i)

    def print_adjl(self):
        """prints out each set of nodes in the graph along with there connections"""
        for i in range(self.prod):
            self.lst[i].print_list()

#R = LinkedList(0, 1, 1)
LIST = AdjList(3, 2)
LIST.print_adjl()
