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
    
    def show(self):
    # 1. Initialize as an empty string, not None
        output = "" 
    
        if self.head is not None:
            current = self.head
            # 2. Loop while current is not None to include the last node
            while current is not None:
                output += str(current.data) + " -> "
                current = current.next
            
            # 3. Print the result (with a little flair for the end of the list)
            print(output + "None")
        else:
            print("La lista está vacía")   
            
    def search_by_element(self, value):
        current = self.head
        position = 0

        while current is not None:
            if current.data == value:
                return position
            current = current.next
            position += 1
        
        return -1  # Indica que no se encontró
    
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

        print(f"The size of the list is {counter}")
    
    def ordenate(self):
        if self.head is None or self.head.next is None:
            return

        change = True
        while change:
            change = False
            current = self.head
            previous = None

            while current.next is not None:
                nxt = current.next 

                try:
                    val_actual = int(current.data)
                    val_siguiente = int(nxt.data)
                except ValueError:
                    val_actual = current.data
                    val_siguiente = nxt.data

                if val_actual > val_siguiente:
                    change = True 
                    
                    if previous is None:
                        self.head = nxt
                    else:
                        previous.next = nxt

                    current.next = nxt.next
                    nxt.next = current

                    # Después del intercambio, el nodo que era el siguiente 
                    # ahora está atrás, así que 'previous' debe ser ese.
                    previous = nxt
                else:
                    # Si no hubo intercambio, simplemente avanzamos
                    previous = current
                    current = current.next

    def delete_by_value(self, value):
        current = self.head
        previous = None

        if current is None:
            print("Esta lista esta vacía")
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
        print("Value not found in the list")

    def invest_list(self):
        current = self.head
        previous = None

        while current is not None:
            next = current.next
            current.next = previous
            previous = current
            current = next

            self.head = previous