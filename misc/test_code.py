
class Node:
    def __init__(self, data):
        self.left_node = None
        self.right_node = None
        self.data = data

    def insert(self, data):
# Compare the new value with the parent node or root node.
        if self.data:
            if data < self.data: #If the value is less than the parent it will be inserted to the left
                if self.left_node is None: 
                    self.left_node = Node(data)
                else:
                    self.left_node.insert(data)
            elif data > self.data: #If the value is less than the parent it will be inserted to the right
                if self.right_node is None:
                    self.right_node = Node(data)
                else:
                    self.right_node.insert(data)
        else:
            self.data = data

    def find_value(self, value):
        """For this problem, your goal is to make a function that will determine if a value is in the tree. 
        The parameter, value, is the number we will be looking for in the tree.  A few hints: 1) Make a base case that will automatically return 
        the value if found, 2) search the left side of the tree and the right side of the tree seperately. 
        The insert function can help provide guidance though it will be a little different. Good luck!"""

        if(self.data == value): #If the number we are looking it matches the one we are looking for we return out of the function with a true.
            return True
        elif value < self.data: #If the number is less than the parent we look on th eleft side of the tree, else we look on the right.
            if self.left_node:
                return self.left_node.find_value(value)
            else:
                return False
        else:
            if self.right_node:
                return self.right_node.find_value(value)
            else:
                return False

# Print the tree after we insert the data
    def print_tree(self):
        if self.left_node:
            self.left_node.print_tree()
        if self.right_node:
            self.right_node.print_tree()
        
        #Print the data
        print(self.data)


def main():


    # Use the insert method to add nodes
    root = Node(12)
    root.insert(0)
    root.insert(5)
    root.insert(3)
    root.insert(34)
    root.insert(50)
    root.print_tree() 


    #------------------------PROBLEM 1 TEST CASES---------------------------
    print()
    print(root.find_value(2)) #False
    print(root.find_value(5)) #True
    print(root.find_value(34)) #True
    print(root.find_value(7)) #False
    print(root.find_value(100)) # False
    print(root.find_value(0)) #True

main()
