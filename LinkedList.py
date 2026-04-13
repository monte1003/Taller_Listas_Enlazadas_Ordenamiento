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

    def buscar(self, valor):
        actual = self.head
        posicion = 0

        while actual is not None:
            if actual.dato == valor:
                return posicion
            actual = actual.next
            posicion += 1

        return -1
    
    def eliminar_primero(self):
        if self.head is None:
            print("La lista está vacía, no se puede eliminar")
        else:
            self.head = self.head.next

    def tamaño(self):
        contador = 0
        actual = self.head

        while actual is not None:
            contador += 1
            actual = actual.next

        return contador
    
    def ordenar(self):
        if self.head is None:
            return

        cambiado = True

        while cambiado:
            cambiado = False
            actual = self.head
            anterior = None

            while actual.next is not None:
                next = actual.next

                if actual.dato > siguiente.dato:
                    # intercambio de nodos (NO de valores)
                    cambiado = True

                    if anterior is None:
                        # intercambiar en la cabeza
                        self.cabeza = siguiente
                    else:
                        anterior.siguiente = siguiente

                    actual.siguiente = siguiente.siguiente
                    siguiente.siguiente = actual

                    # mover anterior
                    anterior = siguiente
                else:
                    anterior = actual
                    actual = actual.siguiente
