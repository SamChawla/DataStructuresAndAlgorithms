
class DLLNode:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

    def __repr__(self):
        return "DLLNode object: data={}".format(self.data)

    def get_data(self):
        """Return the self.data attribute."""
        return self.data

    def set_data(self, new_data):
        """Replace the existing value of the self.data attribute with new_data
        parameter."""
        self.data = new_data

    def get_next(self):
        """Return the self.next attribute"""
        return self.next

    def set_next(self, new_next):
        """Replace the existing value of the self.next attribute with new_next
        parameter."""
        self.next = new_next

    def get_previous(self):
        """Return the self.previous attribute"""
        return self.previous

    def set_previous(self, new_previous):
        """Replace the existing value of the self.previous attribute with
        new_previous parameter."""
        self.previous = new_previous


class DLL:

    def __init__(self):
        self.head = None

    def __repr__(self):
        return "<DLL object: head={}>".format(self.head)

    def is_empty(self):
        return self.head is None

    def size(self):
        """Traverses the Linked List and returns an integer value representing
        the number of nodes in the Linked List.

        The time complexity is O(n) because every Node in the Linked List must
        be visited in order to calculate the size of the Linked List.
        """
        size = 0
        if self.head is None:
            return 0

        current = self.head
        while current is not None:  # While there are still Nodes left to count
            size += 1
            current = current.get_next()

        return size

    def search(self, data):
        """Traverses the Linked List and returns True if the data searched for
        is present in one of the Nodes. Otherwise, it returns False.

        The time complexity is O(n) because in the worst case, we have to visit
        every Node in the list.
        """
        if self.head is None:
            return "Linked List is empty. No Nodes to search."

        current = self.head
        while current is not None:
            if current.get_data() == data:
                return True
            else:
                current = current.get_next()

        return False

    def add_front(self, new_data):
        """Add a Node whose data is the new_data argument to the front of the
        Linked List."""
        temp = DLLNode(new_data)
        temp.set_next(self.head)

        if self.head is not None:
            self.head.set_previous(temp)

        self.head = temp

    def remove(self, data):
        """Removes the first occurence of a Node that contains the data argument
        as its self.data attribute. Returns nothing.

        The time complexity is O(n) because in the worst case, we have to visit
        every Node before finding the one we want to remove.
        """
        if self.head is None:
            return "Linked List is empty. No Nodes to remove."

        current = self.head
        found = False
        while not found:
            if current.get_data() == data:
                found = True
            else:
                if current.get_next() is None:
                    return "A Node with that data value is not present."
                else:
                    current = current.get_next()

        if current.previous is None:
            self.head = current.get_next()
        else:
            current.previous.set_next(current.get_next())
            current.next.set_previous(current.get_previous())
    
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
