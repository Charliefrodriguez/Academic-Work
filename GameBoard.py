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
        self.head = GraphNode.__init__(self, terrain, path_diff, name)
        print(self.head)

    def insert(self, terrain, path_diff, name):
        """This method will insert nodes into our linked list """
        ptr = self.head 
        print(ptr) # this is a test
        while ptr.after is not None:
            ptr = ptr.after

        if ptr.after is None:
            ptr.after = GraphNode(terrain, path_diff, name)

    def print_list(self):
        """ Prints out the members of the linked list """
        ptr = self.head
        while ptr.after is not None:
            print("name "+ptr.name+" "+"terrain "+ptr.terrain)
            ptr = ptr.after
class AdjList:
    """Here we are going to build the adjaceny linked list """
    def __init__(self, x_dim, y_dim):
        self.lst = [LinkedList.__init__(0, 1, i) for i in range(x_dim * y_dim)]

R = LinkedList(0, 1, 1)
R.insert(1, 1.5, 2)
#R.insert(1, 1.5, 3)
#R.print_list()
