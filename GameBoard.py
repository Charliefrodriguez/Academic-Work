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
        """This method will insert nodes into our linked list, without allowing  duplicate keys"""
        ptr = self.head
        while ptr.after is not None:
            if ptr is not None and name is ptr.name:
                print("No duplicate key!")
                return
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
        dim = x_dim * y_dim
        self.dim = dim
        self.lst = [0] * (dim)
        for i in range(dim):
            self.lst[i] = LinkedList(0, 1, i)

    def print_adjl(self):
        """prints out each set of nodes in the graph along with there connections"""
        for i in range(self.dim):
            self.lst[i].print_list()
    def adj_ins(self, list_index, terrain, path_diff, name):
        """This is insert method for our adjacency linked list """
        self.lst[list_index].insert(terrain, path_diff, name)

    def screen(self, array):
        """This method will screen out invalid coordinates"""
        good_val = [0] * 0
        for x in array:
            if x[0] >= 0 and x[1] >= 0 and x[1] < 160 and x[0] < 120:
                good_val.append(x)
        return good_val

    def position(self, value):
        """computes the index of value in the matrix interpreation of the array"""
        flag = False
        for i in range(self.dim):
            if (160 *i <= value and value <= 160*i + 159):
                indx = i
                flag = True
                break
        if flag is False:
            return [-1, -1]
        else:
            j = -indx*160 +  value
            if j >= 0:
                return [indx, j]
            return [-1, -1]

    def inv_position(self, i, j):
        """Converts position back to an array value"""
        return j + i * 160

    def connect(self):
        """This method links the graph together in the gameboard config """
        for i in range(self.dim):
            pos = self.position(i)
            n_c = [[pos[0]-1, pos[1]], [pos[0]+1, pos[1]], [pos[0], pos[1]+1], [pos[0],\
            pos[1]-1], [pos[0]-1, pos[1]+1], [pos[0]+1, pos[1]-1], [pos[0]-1, pos[1]-1]\
            , [pos[0]+1, pos[1]+1]]
            neighboors = [self.inv_position(x[0], x[1]) for x in self.screen(n_c)]
            # neighboors = [self.inv_position(x[0], x[1]) for x in n_c]
            if i is 159: print(n_c)
            for x in neighboors:
                if x < 0:
                    continue
                self.adj_ins(i, 0, 1, x)
#R = LinkedList(0, 1, 1)
LIST = AdjList(160, 120)
#LIST.adj_ins(4, 2, 2, 6)
LIST.connect()
#print(LIST.position(159))
#print(LIST.position(160))
#LIST.lst[0].print_list()
#print(" ")
LIST.lst[0].after.terrain = 1
print(LIST.lst[0].after.terrain)
LIST.lst[0].print_list()
#print(" ")
#LIST.lst[160].print_list()
#print(" ")
#LIST.lst[19199].print_list()
#print(LIST.screen([[-1, 159], [0, 160], [0, 158], [-1, 160], [-1, 158]]))
