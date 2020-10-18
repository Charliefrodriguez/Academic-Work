import queue
import GameBoard

#List = GameBoard.AdjList(160, 120)

def astarAlgo(start_node, end_node, List):
   open_list = []
   closed_list = []
   open_list.append(start_node)  
   path = []

   while len(open_list) > 0:
      #Find the node with the lowest f cost
      current_node = open_list[0]
      print(current_node.name)
      current_index = 0
      for index, item in enumerate(open_list):
         if item.f <= current_node.f:
               current_node = item
               current_index = index
      
      path.append(current_node.name)
      # Pop current off open list, add to closed list
      open_list.pop(current_index) #get rid of the thing at position current_index
      closed_list.append(current_node)
      # Found the goal
      if current_node == end_node:
         #print(path) 
         return path
       #  path = []
       #  current = current_node
       #  while current is not None:
       #        path.append(List.position(current.name))
       #        current = current.after
       #  return path[::-1] # Return reversed path
      #Generate neighbors
      neighboors = []
      ptr  = List.lst[current_node.name].head
      while ptr != None:
         #print("woops")
         if ptr.terrain != 0: 
                neighboors.append(ptr)
         ptr = ptr.after           
      
      for nei in neighboors: 
          print( "["+str(List.position(nei.name)[0]) +", " +str(List.position(nei.name)[1]) + "]" + "transition cost "+ str(nei.path_diff)) 
      
      print("\n") 

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

#value = [List.set_startgoal()[0],List.set_startgoal()[1]] 
#print(" ")
#print("Here is the start value "+ str(value[0]) + " " + "Here is the goal value " + str(value[1]))
#print("This is the node value" + str( List.lst[   value[0] ].head.name))

#out  = astarAlgo(List.lst[ 0 ].head,  List.lst[ 483 ].head , List)
#print("This is the path\n")
#print(out)
