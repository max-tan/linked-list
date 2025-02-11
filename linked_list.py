# Define a Node class to represent a single node in a linked list
class Node:
    def __init__(self):
        # The previous node reference (used in doubly linked lists)
        self.prev = ''
        # The element (data) stored in the node
        self.elem = None
        # The next node reference
        self.next = None

    # Function to return the node's representation in list form
    def node(self):
        # If prev is empty (used as an indicator for singly linked lists)
        if self.prev == '':
            return [self.elem, self.next]  # Return only the element and next reference
        return [self.prev, self.elem, self.next]  # Return prev, element, and next for doubly linked lists
    

# Define a linked list class that supports different types of linked lists
class linkedList:
    def __init__(self):
        # Store the elements of the linked list in a standard list
        self.array = []
        # Default type of linked list (singly regular)
        self.type = "singly regular"

        # Supported types:
        # - singly regular (linear singly linked list)
        # - doubly regular (linear doubly linked list)
        # - singly circular (circular singly linked list)
        # - doubly circular (circular doubly linked list)

    # Method to set the type of the linked list
    def set(self, type: str):
        self.type = type
        
    # Method to add an element to the linked list
    def add(self, elem):
        self.array.append(elem)

    # Method to generate and print the linked list structure based on the set type
    def output(self):
        # Store the final linked list representation
        self.linkedList = []

        # Case: Singly Regular Linked List
        if self.type == "singly regular":
            # Loop through elements except the last one
            for i in range(len(self.array) - 1):
                node = Node()
                node.elem = self.array[i]  # Assign the current element
                node.next = self.array[i+1]  # Link to the next element
                self.linkedList.append(node.node())  # Store node representation

            # Handle the last node (its next should be None)
            node = Node()
            node.elem = self.array[-1]
            node.next = None  # End of the list
            self.linkedList.append(node.node())
                
        # Case: Doubly Regular Linked List
        elif self.type == "doubly regular":
            # Loop through elements except the last one
            for i in range(len(self.array) - 1):
                if i == 0:
                    # First node (no previous node)
                    node = Node()
                    node.prev = None  # First node has no previous node
                    node.elem = self.array[i]
                    node.next = self.array[i+1]  # Link to the next node
                    self.linkedList.append(node.node())
                else:
                    # Middle nodes
                    node = Node()
                    node.prev = self.array[i-1]  # Link to the previous node
                    node.elem = self.array[i]
                    node.next = self.array[i+1]  # Link to the next node
                    self.linkedList.append(node.node())

            # Handle the last node (its next should be None)
            node = Node()
            node.prev = self.array[-2]  # Link to the second-to-last element
            node.elem = self.array[-1]
            node.next = None  # End of the list
            self.linkedList.append(node.node())
            
        # Case: Singly Circular Linked List
        elif self.type == "singly circular":
            # Loop through elements except the last one
            for i in range(len(self.array) - 1):
                node = Node()
                node.elem = self.array[i]
                node.next = self.array[i+1]  # Link to the next node
                self.linkedList.append(node.node())

            # Handle the last node (it should point back to the first element)
            node = Node()
            node.elem = self.array[-1]
            node.next = self.array[0]  # Circular link to the first node
            self.linkedList.append(node.node())    

        # Case: Doubly Circular Linked List
        elif self.type == "doubly circular":
            # Loop through elements except the last one
            for i in range(len(self.array) - 1):
                if i == 0:
                    # First node (previous points to last node)
                    node = Node()
                    node.prev = self.array[-1]  # Circular link to last node
                    node.elem = self.array[i]
                    node.next = self.array[i+1]  # Link to next node
                    self.linkedList.append(node.node())
                else:
                    # Middle nodes
                    node = Node()
                    node.prev = self.array[i-1]  # Link to previous node
                    node.elem = self.array[i]
                    node.next = self.array[i+1]  # Link to next node
                    self.linkedList.append(node.node())

            # Handle the last node (next should link to the first, prev to second-to-last)
            node = Node()
            node.prev = self.array[-2]  # Link to previous node
            node.elem = self.array[-1]
            node.next = self.array[0]  # Circular link to the first node
            self.linkedList.append(node.node())

        # Print the final linked list representation
        print(self.linkedList)


# Example Usage
test = linkedList()
test.set("doubly circular")  # Set the type to doubly circular
test.add(1)  # Add elements to the linked list
test.add(2)
test.add(3)
test.add(4)
test.output()  # Generate and print the linked list
