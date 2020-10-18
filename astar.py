import queue
import GameBoard.py 

def astarAlgo(start_node, end_node, List):
   open_list = []
   closed_list = []
   open_list.append(start_node)
   while len(open_list) > 0:
      #Find the node with the lowest f cost
      current_node = open_list[0]
      current_index = 0
      for index, item in enumerate(open_list):
         if item.f < current_node.f:
               current_node = item
               current_index = index
      # Pop current off open list, add to closed list
      open_list.pop(current_index) #get rid of the thing at position current_index
      closed_list.append(current_node)
      # Found the goal
      if current_node == end_node:
         path = []
         current = current_node
         while current is not None:
               path.append(current.position)
               current = current.parent
         return path[::-1] # Return reversed path
      #Generate neighbors
      neighboors = []
      ptr  = List.lst[current.name].head
      while ptr != None:
         if ptr.terrain != 0 and ptr not in closed_list: 
                neighboors.append(ptr)
      ptr = ptr.after           
      # Loop through neighbors
      for neighboor in neighboors:
         # Neighbor is on the closed list
         for closed_neighbor in closed_list:
               if neighboor == closed_neighbor:
                  continue
         # Create the f, g, and h values
         neighboor.g = current_node.g + 1
         neighboor.h = ((List.position(neighboor.name)[0] - List.position(end_node.name)[0]) ** 2) + ((List.position(neighboor.name)[1] - List.position(end_node.name)[1]) ** 2)
         neighboor.f = neighboor.g + neighboor.h
         neighboor.g = current_node.g + 1
         neighboor.h = ((List.position(neighboor.name)[0] - List.position(end_node.name)[0]) ** 2) + ((List.position(neighboor.name)[1] - List.position(end_node.name)[1]) ** 2)
         neighboor.f = neighboor.g + neighboor.h
         # Neighbor is already in the open list
         for open_node in open_list:
               if neighboor == open_node and neighboor.g > open_node.g:
                  continue
         # Add the neighboor to the open list
         open_list.append(neighboor)

if __name__ == "__main__":
    pass
