inventario = {}
carrito = []


print("Bienvenido al sistema ELias")
eleccion = input("Usted es un cliente o un administrador?: ").lower().strip()
if eleccion == "administrador":

    while True:
        menu = input(
            "Que desea hacer?: 1.Agregar productos  2.Borrar producto  3.Cambiar el precio de un productoo  4. Revisar invetario  5. Salir:                            ")
        if menu == "1":
            producto = input(
                "Ingrese el nombre del producto que desea agregar: ").lower().strip()
            try:
                precio = float(input("Ingrese el precio del producto: "))
                cantidad = int(input("Ingrese la cantidad del producto: "))
                inventario[producto] = {
                    "precio": precio,
                    "stock": cantidad
                }
                print("Producto agregado con exito")
            except ValueError:
                print("Ingresa un valor numerico")
        elif menu == "2":
            producto = input(
                "Ingrese el nombre del producto que desea borrar: ").lower().strip()
            if producto in inventario:
                del inventario[producto]
                print("El producto a sido eliminado con exito")
            else:
                print("El producto", producto,
                      "no se encuentra en el inventario")

        elif menu == "3":
            try:
                producto = input(
                    "Ingrese el nombre del producto al que desea cambiarle el precio: ")
                if producto in inventario:
                    print(producto)
                    nuevo_precio = float(input(" Ingrese el nuevo valor:  "))
                    inventario[producto]["precio"] = nuevo_precio
                    print("Precio actualizado con exito")
                else:
                    print("El producto no se encuentra en el inventario")
            except ValueError:
                print("Errror, por favor ingresa un valor numerico")

        elif menu == "4":
            if len(inventario) == 0:
                print("Error el inventario esta vacio")
            else:
                print("--- INVENTARIO ACTUAL ---")
                for nombre, datos in inventario.items():
                    print(
                        f"Producto: {nombre.capitalize()}, Precio: ${datos['precio']}, Cantidad: {datos['stock']}")

        elif menu == "5":
            print("Saliendo del sistema de administrador.")
            break
        else:
            print("Opcion no valida, por favor intente de nuevo")

elif eleccion == "cliente":
    print("Bienvenido a la tienda, por el momento este es nuestro inventario actual:")
    if len(inventario) == 0:
        print("Lo sentimos, no hay productos disponibles por el momento.")
    else:
        lista_productos = list(inventario.keys())
        contador = 1
        for nombre in lista_productos:
            precio = inventario[nombre]["precio"]
            print(f"{contador}. {nombre.capitalize()} - ${precio}")
            contador += 1
        try:
            opcion = int(input("Ingrese el numero del producto que desea:  "))
            if 1 <= opcion <= len(lista_productos):
                producto_elegido = lista_productos[opcion - 1]
                stock_disponible = inventario[producto_elegido]["stock"]

                try:
                    cantidad = int(
                        input("Porfavor ingrese la cantidad que necesita: "))
                    if cantidad <= stock_disponible:
                        carrito[producto_elegido] = cantidad
                        print(
                            f"Se agregaron {cantidad} {producto_elegido}(s) al carrito.")

                        precio = inventario[producto_elegido]["precio"]
                        total = cantidad * precio
                        inventario[producto_elegido]["stock"] = stock_disponible - cantidad

                        print("Su total a pagar es:", total)
                        print("Gracias por su compra")
                    else:
                        print(
                            f"No hay suficiente stock. Solo nos quedan {stock_disponible} unidades.")
                except ValueError:
                    print("Por favor solo ingrese numeros, no letras")
            else:
                print("opcion invalida, por favor elige un numero dentro del parametro", len(
                    lista_productos))
        except ValueError:
            print("Por favor solo ingrese numeros, no letras")
