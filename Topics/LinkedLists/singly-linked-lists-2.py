class SLLNode:

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return "SLLNode object: data={}".format(self.data)

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

# if __name__  == "__main__":
#     # Initialize two nodes
#     node = SLLNode('node1')
#     node2 = SLLNode('node2')
#
#     # Check if next node is available
#     node.get_next()
#
#     # Set next node
#     node.set_next(node2)
#
#     # Now check next node
#     node.get_next()