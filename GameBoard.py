"""We are going to build our graph node class here"""
import random as rnd
import math as m
#import numpy as np
#We are going to experiment a bit with classes and nodes
# pylint: disable=R0201
# pylint: disable=R1705
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
        if ptr.name == name: 
           # print("no duplicate keys")
            return 
        while ptr.after is not None:
            if ptr != None and name == ptr.name:
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

    def print_list(self,):
        """ Prints out the members of the linked list """
        ptr = self.head
        count = 0
        while ptr is not None:
            count+=1
            print("name " + str(ptr.name) + " " + "terrain " + str(ptr.terrain))
            ptr = ptr.after
        print("len of list "+str(count))
class AdjList:
    """Here we are going to build the adjaceny linked list """
    def __init__(self, x_dim, y_dim):
        dim = x_dim * y_dim
        self.dim = dim
        self.lst = [0] * (dim)
        for i in range(dim):
            self.lst[i] = LinkedList(1, 1, i)
        self.connect()
        for i in range(8):
            self.set_subgrid()

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
        if i >= 120 or i < 0:
            return -1
        if j > 160 or j < 0:
            return -1
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
                self.adj_ins(i, 1, 1, x)

    def set_subgrid(self):
        """sets up the 31x31 subgrid"""
        i = self.random_coor()[0]
        j = self.random_coor()[1]
        #print("["+ str(i) +","+ str(j) +"]")
        c_one = 0
        while c_one < 31:
            c_two = 0
            while c_two < 31:
                out = self.inv_position(i - 15 + c_one, j - 15 + c_two)
                #print(out)
#                print(str(i-15+c_one) +" "+ str(j-15 +c_two))
                ter_list = [1, 2]
                ter_weight = [.50, .50]
                ter_dif = rnd.choices(ter_list, ter_weight)
                self.set_all(out, 1 if ter_dif[0] == 1 else 2)
                c_two += 1
            c_one += 1

    def random_coor(self):
        """generates random coordinates for 31x31 subgrid"""
        i = rnd.randint(30, 88)
        j = rnd.randint(30, 128)
        return [i, j]

    def highway_start(self):
        """This function will select the start point of the highway"""
        i = rnd.randint(0, 120)
        if i == 0 or i == 120:
            j = rnd.randint(1, 118) #we don't want the map corners
        else:
            j = rnd.choice([0, 119])
        return [i, j]

    def highway_mov(self, prev_dir):
        """This will return the direction which the highway will go in """

        set_dir = ['s', 'p']
        distro = [.60, .20]
        direction = rnd.choices(set_dir, distro)
        if direction == 's':
            if prev_dir == 'd':
                return 'd'
            elif prev_dir == 'u':
                return 'u'
            elif prev_dir == 'l':
                return 'l'
            else:
                return 'r'
        else:
            if prev_dir == 'd':
                return 'r'
            elif prev_dir == 'u':
                return 'l'
            elif prev_dir == 'l':
                return 'u'
            else:
                return 'd'



    def path_node_check(self, arr_of_paths, name):
        """Checks that all nodes inserted into the list don't collide with existing paths """
        if name == -1: # check for invalid coordinates
            return 'c'

        if len(arr_of_paths) == 0:
            return 'o'

        for path in arr_of_paths:
            ptr = path.head
            flag = 'o'
            while ptr != None:
                if ptr.name == name:
                    flag = 'c'
                    break
                ptr = ptr.after

            if flag == 'c':
                return 'c'
            else:
                return 'o'


    def is_boundary(self, i, j):
        """checks if index value is at the boundary of map """
        if i == 0 or i == 119:
            return 0
        elif j == 0 or j == 160:
            return 0
        else:
            return 1


    def highway_set(self):
        """This function will set up the 4 highways on the map """
        arr_paths = [None]*0
       # abort =0
        while len(arr_paths) < 4:
        #    abort += 1
            coor = self.highway_start()
            path_len = 0
            if coor[0] == 0:
                direction = 'd'
            elif coor[0] == 119:
                direction = 'u'
            elif coor[1] == 0:
                direction = 'r'
            else:
                direction = 'l'
           # print("["+ str(coor[0])+ "," + str(coor[1]) + "]")
            position = self.inv_position(coor[0], coor[1])

            path = LinkedList(self.lst[position].head.terrain, self.lst[position].head.path_diff,
                        self.lst[position].head.name)
         #this is to do the initial iteration at the boundary
            cur_pos = [coor[0], coor[1]]
         #   safety =0
            flag = 0
            print(" ")
            path.print_list()
            print(direction + "\n")

           # while path_len < 100:
            while self.is_boundary(cur_pos[0],cur_pos[1]):
          #      safety = safety +1 
 #               print(" ")
#                path.print_list()
           #     if safety == 7:
            #        break
                if direction == 'd':
                    for i in range(20):
                        temp_pos = self.inv_position(cur_pos[0]+i, cur_pos[1])
  #                      print("[" +str(cur_pos[0]+i)+ "," +str(cur_pos[1]) + "]")
                        rating = self.path_node_check(arr_paths, temp_pos)
                        if rating == 'c':
                            flag = 1
                            break
                        path.insert(self.lst[temp_pos].head.terrain, self.lst[temp_pos].head.path_diff
                                    , self.lst[temp_pos].head.name)
                    if flag:
                        break
                    cur_pos = [cur_pos[0]+19, cur_pos[1]]

                elif direction == 'u':
                    for i in range(20):
                        temp_pos = self.inv_position(cur_pos[0]-i,  cur_pos[1])
   #                     print("[" +str(cur_pos[0]-i)+ ","+ str(cur_pos[1]) + "]")
                        rating = self.path_node_check(arr_paths, temp_pos)
                        if rating == 'c':
                            flag = 1
                            break
                        path.insert(self.lst[temp_pos].head.terrain, self.lst[temp_pos].head.path_diff
                                    , self.lst[temp_pos].head.name)
                    if flag:
                        break
                    cur_pos = [cur_pos[0]-19, cur_pos[1]]

                elif direction == 'l':
                    for i in range(20):
                        temp_pos = self.inv_position(cur_pos[0], cur_pos[1]-i)
    #                    print("[" +str(cur_pos[0])+ ","+ str(cur_pos[1]-i) + "]")
                        rating = self.path_node_check(arr_paths, temp_pos)
                        if rating == 'c':
                            flag = 1
                            break
                        path.insert(self.lst[temp_pos].head.terrain, self.lst[temp_pos].head.path_diff
                                    , self.lst[temp_pos].head.name)
                    if flag:
                        break
                    cur_pos = [cur_pos[0], cur_pos[1]-19]

                else:
                    for i in range(20):
                        temp_pos = self.inv_position(cur_pos[0], cur_pos[1]+i)
     #                   print("[" +str(cur_pos[0])+ "," +str(cur_pos[1]+i) + "]")
                        rating = self.path_node_check(arr_paths, temp_pos)
                        if rating == 'c':
                            flag = 1
                            break
                        path.insert(self.lst[temp_pos].head.terrain, self.lst[temp_pos].head.path_diff
                                    , self.lst[temp_pos].head.name)
                    if flag:
                        break
                    cur_pos = [cur_pos[0], cur_pos[1]+19]

                direction = self.highway_mov(direction)
                path_len += 20
                print(path_len)
     #       if abort == 5:
     #           break
            if flag and path_len > 100:
                arr_paths.append(path)
            else:
                continue

        return arr_paths

    def initialize_h(self):
        """Intialize the random highways"""
        out = self.highway_set()
        for path in out:
            ptr = path.head
            while ptr != None:
                if self.lst[ptr.name].head.name == 1:
                    self.set_all(ptr.name, 'a')
                else:
                    self.set_all(ptr.name, 'b')
                ptr = ptr.after



#R = LinkedList(0, 1, 1)
#R.insert(0,1,1)
#R.print_list()
LIST = AdjList(160, 120)
#LIST.adj_ins(4, 2, 2, 6)
OUT = LIST.highway_set()
print(len(OUT))
OUT[0].print_list()
OUT[1].print_list()
OUT[2].print_list()
OUT[3].print_list()
LIST.initialize_h()
LIST.print_adjl()
#print(OUT[0].head.after.name)
#print(OUT[2].head.name)
#print(OUT[3].head.name)
#print(LIST.position(159))
#print(LIST.position(160))
#LIST.set_subgrid(31, 31)
#LIST.lst[4991].print_list()
#LIST.lst[4992].print_list()
#LIST.set_subgrid()
#print(LL.head.after)
#print(LIST.screen([[-1, 159], [0, 160], [0, 158], [-1, 160], [-1, 158]]))
