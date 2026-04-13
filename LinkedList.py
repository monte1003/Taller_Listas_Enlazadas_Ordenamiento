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
                output += str(current.data)
                current = current.next
        else:
            print("La lista estas vacia")    
            
    def look(self, value):
        current = self.head
        position = 0

        while current is not None:
            if current.data == value:
                return position
            current = current.next
            position += 1

        return -1
    
    def delete_first_element(self):
        if self.head is None:
            print("La lista está vacía, no se puede eliminar")
        else:
            self.head = self.head.next

    def size(self):
        counter = 0
        current = self.head

        while current is not None:
            counter += 1
            current = current.next

        return counter
    
    def ordenate(self):
        if self.head is None:
            return

        change = True

        while change:
            change = False
            current = self.head
            previous = None

            while current.next is not None:
                next = current.next

                if current.data > next.data:
                    # intercambio de nodos (NO de valores)
                    cambiado = True

                    if previous is None:
                        self.head = next
                    else:
                        previous.next = next

                    current.next = next.next
                    next.next = current

                    # mover anterior
                    previous = next
                else:
                    previous = current
                    current = current.next
