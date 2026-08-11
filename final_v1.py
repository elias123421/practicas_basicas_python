productos = ["mango", "platano", "uva"]
precios = [23, 34, 31]
cantidades = [12, 23, 43]
carrito_compras = []


def mostrar_inventario(lista_prod, lista_prec, lista_cant):
    if len(lista_prod) == 0:
        print("El inventario está vacío.")
    else:
        print("--- INVENTARIO ACTUAL ---")
        for i in range(len(lista_prod)):
            print(
                f"{i + 1}. Producto: {lista_prod[i]}, Precio: ${lista_prec[i]}, Cantidad: {lista_cant[i]}")


print("Bienvenido al sistema ELias")
eleccion = input("Usted es un cliente o un administrador?: ").lower().strip()
if eleccion == "administrador":
    while True:
        menu = input(
            "Que desea hacer?: 1.Agregar productos  2.Borrar producto  3.Cambiar el precio de un productoo  4. Revisar invetario  5. Salir:                            ")
        if menu == "1":
            producto = input(
                "Ingrese el nombre del producto que desea agregar: ").lower().strip()
            productos.append(producto)
            precio = float(input("Ingrese el precio del producto: "))
            precios.append(precio)
            cantidad = int(input("Ingrese la cantidad del producto: "))
            cantidades.append(cantidad)
            print("Producto agregado con exito")
        elif menu == "2":
            producto = input(
                "Ingrese el nombre del producto que desea borrar: ").lower().strip()
            if producto in productos:
                index = productos.index(producto)
                productos.pop(index)
                precios.pop(index)
                cantidades.pop(index)
                print("Producto borrado con exito")
            else:
                print("El producto no se encuentra en el inventario")
        elif menu == "3":
            producto = input(
                "Ingrese el nombre del producto al que desea cambiarle el precio: ")
            if producto in productos:
                index = productos.index(producto)
                nuevo_precio = float(
                    input("Ingrese el nuevo precio del producto: "))
                precios[index] = nuevo_precio
                print("Precio actualizado con exito")
            else:
                print("El producto no se encuentra en el inventario")
        elif menu == "4":
            mostrar_inventario(productos, precios, cantidades)

        elif menu == "5":
            print("Saliendo del sistema de administrador.")
            break
        else:
            print("Opcion no valida, por favor intente de nuevo")
elif eleccion == "cliente":
    print("Bienvenido a la tienda, por el momento este es nuestro inventario actual:")
    mostrar_inventario(productos, precios, cantidades)

    while True:
        compra = input(
            "¿Qué número de producto desea ordenar? (o '0' para seguir a la caja): ").strip()

        if compra == "0":
            print("Pasando a la caja...")
            break

        indice = int(compra) - 1

        if 0 <= indice < len(productos):
            producto_elegido = productos[indice]
            carrito_compras.append(producto_elegido)
            print(f"¡Agregaste '{producto_elegido}' a tu carrito!")
        else:
            print("Número de producto no encontrado. Intente de nuevo.")

    while True:
        print("Bienvenido a la caja")
        break
