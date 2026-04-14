from LinkedList import LinkedList
from Node import Node
def menu():
    list = LinkedList()

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
                list.insert_at_beginning(new_node)

            case 2:
                data = int(input("Ingrese la data del nuevo nodo: "))
                new_node = Node(data)
                list.insert_at_end(new_node)
                

            case 3:
                list.show()

            case 4:
                data_search = int(input("Ingrese la data del nodo a buscar: "))
                num = list.search_by_element(data_search)
                if num == -1:
                    print("The element can't exist")
                else:
                    print(f"The position of the element is {num}")

            case 5:
                list.delete_first_element()

            case 6:
                print("Eliminar por valor")
                value_to_eliminated = int(input("Ingrese el valor a eliminar: "))
                list.delete_by_value(value_to_eliminated)

            case 7:
                print("Tamaño de la lista")
                list.size()

            case 8:
                print("Invertir lista")
                list.invest_list()

            case 9:
                print("Ordenar lista")
                list.ordenate()

            case 0:
                print("Saliendo...")
                break

            case _:
                print("Opción inválida")

menu()