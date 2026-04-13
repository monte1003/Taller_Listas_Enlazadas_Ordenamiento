from LinkedList import LinkedList
from Node import Node
def menu():
    lista = LinkedList()

    while True:  
        print("\n1. Insertar al inicio")
        print("2. Insertar al final")
        print("3. Mostrar lista")
        print("4. Buscar elemento")
        print("5. Eliminar primer elemento")
        print("6. Eliminar por valor")
        print("7. Tamaño de la lista")
        print("8. Invertir lista")
        print("9. Ordenar lista")
        print("0. Salir")

        opcion = int(input("Seleccione una opción: "))

        match opcion:
            case 1:
                print("Insertar al inicio")
                data = input("Ingrese la data del nuevo nodo: ")
                new_node = Node(data)
                lista.insert_at_beginning(new_node)

            case 2:
                data = input("Ingrese la data del nuevo nodo: ")
                new_node = Node(data)
                lista.insert_at_end(new_node)
                

            case 3:
                lista.show()

            case 4:
                print("Buscar elemento")

            case 5:
                print("Eliminar primer elemento")

            case 6:
                print("Eliminar por valor")
                valor = int(input("Ingrese el valor a eliminar: "))
                lista.eliminar_por_valor(valor)

            case 7:
                print("Tamaño de la lista")
                print("Tamaño de la lista:", lista.tamaño())

            case 8:
                print("Invertir lista")
                lista.invertir_lista()

            case 9:
                print("Ordenar lista")

            case 0:
                print("Saliendo...")
                break

            case _:
                print("Opción inválida")

menu()