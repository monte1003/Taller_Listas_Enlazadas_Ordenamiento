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
    def mostrar_lista(self):
        actual = self.head
        while actual:
            print(actual.data)
            actual = actual.next

            print ("Lista vacía")

    def eliminar_por_valor(self, valor):
        actual = self.head
        anterior = None

        if actual is None:
            print("Esta lista esta vacía")
            return
        
        if actual.data == valor:
            self.head = actual.next
            return
        
        while actual is not None:
            if actual.data == valor:
                anterior.next = actual.next
                return
            anterior = actual
            actual = actual.next
            print("Valor no encontrado en la lista")

    def invertir_lista(self):
        actual = self.head
        anterior = None

        while actual is not None:
            siguiente = actual.next
            actual.next = anterior
            anterior = actual
            actual = siguiente

            self.head = anterior 