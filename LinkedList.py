from Node import Node
class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        
        current = self.head
        while current.next is not None:
            current = current.next
        
        current.next = new_node
    
    def show(self, data):
        output = None
        if(self.head is not None):
            current = self.head
            while current.next is not None:
                output += str(curre.data)
                current = current.next
        else:
            print("La lista estas vacia") 

    def delete_value(self, value):
        current = self.head
        previous = None

        if current is None:
            print("Esta lista está vacía")
            return
        
        if current.data == value:
            self.head = current.next 
            return
        
        while current is not None:
            if current.data == value:
                previous.next = current.next 
                return
            
            previous = current
            current = current.next
            
        print("Valor no encontrado en la lista")

    def reverse_list(self):
        current = self.head
        previous = None

        while current is not None:
            next_node = current.next
            
            current.next = previous
            
            previous = current
            current = next_node

        self.head = previous
