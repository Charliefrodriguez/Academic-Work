"""We are going to build our graph node class here"""
import random as rnd
import math as m
#import numpy as np
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

    def set_path(self, value):
        """sets path diff for Graph Node """
        self.path_diff = value

    def set_ter(self, value):
        """sets terrain type for Graph Node """
        self.terrain = value
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

    def set_attr(self, attr, name, value):
        """sets terrain and path_diff attributes of nodes in LL"""
        ptr = self.head
        flag = False
        while ptr is not None:
            if ptr.name == name:
                flag = True
                break
            ptr = ptr.after

        if flag:
            if attr == "ter":
                ptr.set_ter(value)
            elif attr == "path":
                ptr.set_path(value)
            else:
                print("not an attribute")
        else:
            print("not in list")

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
            self.lst[i] = LinkedList(1, 1, i)

    def print_adjl(self):
        """prints out each set of nodes in the graph along with there connections"""
        for i in range(200):
            print("List"+str(i)+ "\n")
            self.lst[i].print_list()
            print(" ")

    def adj_ins(self, list_index, terrain, path_diff, name):
        """This is insert method for our adjacency linked list """
        self.lst[list_index].insert(terrain, path_diff, name)

    def set_all(self, target, ter_val):
        """This method will set ter_val for all occurances of name in all adj linked lists """
        self.lst[target].set_attr("ter", target, ter_val)
        ptr = self.lst[target].head
        while ptr != None:
            self.lst[ptr.name].set_attr("ter", target, ter_val)
            ptr = ptr.after

    def screen(self, array):
        """This method will screen out invalid coordinates"""
        good_val = [0] * 0
        for x in array:
            if x[0] >= 0 and x[1] >= 0 and x[1] < 160 and x[0] < 120:
                good_val.append(x)
        return good_val

    def position(self, value):
        """computes the index of value in the matrix interpreation of the array"""
        #flag = False
        #for i in range(self.dim):
        #    if (160 *i <= value and value <= 160*i + 159):
        #        indx = i
        #        flag = True
        #        break
       # if flag is False:
       #     return [-1, -1]
       # else:
        indx = m.floor(value/160)
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
            if i == 159:
                print(n_c)
            for x in neighboors:
                if x < 0:
                    continue
                self.adj_ins(i, 0, 1, x)

    def set_subgrid(self):
        """sets up the 31x31 subgrid"""
        i = self.random_coor()[0] 
        j = self.random_coor()[1]
        c_one = 0
        while c_one < 31:
            c_two = 0
            while c_two < 31:
                out = self.inv_position(i - 15 + c_one, j - 15 + c_two)
                print(out)
#                print(str(i-15+c_one) +" "+ str(j-15 +c_two))
                ter_list = [1, 2]
                ter_weight = [.50, .50]
                ter_dif = rnd.choices(ter_list, ter_weight)
                self.set_all(out, 1 if ter_dif[0] == 1 else 2)
                c_two += 1
            c_one += 1

    def random_coor(self):
        """generates random coordinates for 31x31 subgrid"""
        i = rnd.randint(31, 89)
        j = rnd.randint(31, 129)
        return [i, j]

#R = LinkedList(0, 1, 1)
LIST = AdjList(160, 120)
#LIST.adj_ins(4, 2, 2, 6)
LIST.connect()
#print(LIST.position(159))
#print(LIST.position(160))
#LIST.set_subgrid(31, 31)
#LIST.lst[4991].print_list()
LIST.print_adjl()
#LIST.lst[4992].print_list()
#LL = LinkedList(1, 1, 0)
#LL.insert(1, 1, 1)
#LIST.print_adjl()
#print(LL.head.after)
#print(LIST.screen([[-1, 159], [0, 160], [0, 158], [-1, 160], [-1, 158]]))
