
class DLLNode:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

    def __repr__(self):
        return "DLLNode object: data={}".format(self.data)

    def get_data(self):
        """
        Return the self.data attribute.
        """
        return self.data

    def set_data(self, new_data):
        """
        Replace the existing data with new data
        """
        self.data = new_data

    def get_next(self):
        """
        Return the self.next attribute.        
        """
        return self.next

    def set_next(self, new_next):
        """
        Replace the existing next with new_next
        """
        self.next = new_next
    
    def get_previous(self):
        """
        Return the self.previous attribute.        
        """
        return self.previous

    def set_previous(self, new_previous):
        """
        Replace the existing previous with new_previous
        """
        self.previous = new_previous

    
# if __name__  == "__main__":
#     # Initialize three nodes
#     node = DLLNode('node1')
#     node2 = DLLNode('node2')
#     node3 = DLLNode('node3')

#     # Check if next and previous nodes are available
#     node.get_next()
#     node.get_previous()

#     # Set next and previous nodes
#     node.set_next(node3)
#     node.set_previous(node2)

#     # Now check nodes
#     node.get_next()
#     node.get_previous()
