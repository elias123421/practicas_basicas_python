inventario = []
contador = 0

for i in range(5):
    producto = input("ingrese el producto que desee agregar:")
    inventario.append(producto)

print("Mi inventario")
for producto in inventario:
    contador = contador + 1
    print(contador, producto)

print("Si desea salir del programa escriba 'salir'")

while True:
    buscar = input("Que producto esta buscando?: ")
    if buscar == "salir":
        print("Gracias por su visita")
        break
    if buscar in inventario:
        print("Contamos con ese producto", buscar, "numerado como", inventario.index(buscar) + 1)
    else:
        print("No contamos con ese producto en este momento")
    
