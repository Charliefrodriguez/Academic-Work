"""We are going to build our graph node class here"""
#FRUITS_ARRAY = ["hello", "world"]
#for x in FRUITS_ARRAY:
#    print(x)

#We are going to experiment a bit with classes and nodes
class GraphNode:
    """This is my first experiment with a class"""
    def __init__(self, terrain, left, right, above, below):
        self.terrain = terrain
        self.left = left
        self.right = right
        self.above = above
        self.below = below

    def print_graph(self):
        """prints the graph"""
        print(self.left)
