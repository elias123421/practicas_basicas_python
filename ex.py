mascotas = []
contador = 0
for i in range(4):
    mascota = input("Ingresa el nombre de 4 mascotas: ")
    mascotas.append(mascota)

print("Mis mascotas")
for mascota in mascotas:
    contador = contador + 1
    print(contador, mascota)
