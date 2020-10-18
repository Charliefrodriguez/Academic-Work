import queue
import GameBoard.py 

def astarAlgo(startNode, endNode, List):
   open_list = []
   closed_list = []
   open_list.append(startNode)
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
      for neighbor in neighbors:
         # Neighbor is on the closed list
         for closed_neighbor in closed_list:
               if neighbor == closed_neighbor:
                  continue
         # Create the f, g, and h values
         neighbor.g = current_node.g + 1
         neighbor.h = ((List.position(neighboor.name)[0] - List.position(end_node.name)[0]) ** 2) + ((List.position(neighboor.name)[1] - List.position(end_node.name)[1]) ** 2)
         neighbor.f = neighbor.g + neighbor.h
         # Neighbor is already in the open list
         for open_node in open_list:
               if neighbor == open_node and neighbor.g > open_node.g:
                  continue
         # Add the neighbor to the open list
         open_list.append(neighbor)

if __name__ == "__main__":
    pass
