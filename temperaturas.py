# Matriz 3D: [ciudad][semana][día]
# Ejemplo: 2 ciudades, 2 semanas, 7 días por semana
temperaturas = [
    [   # Ciudad 1
        [30, 32, 31, 29, 28, 27, 26],  # Semana 1
        [25, 27, 26, 28, 29, 30, 31]   # Semana 2
    ],
    [   # Ciudad 2
        [20, 22, 23, 21, 19, 18, 20],  # Semana 1
        [24, 23, 22, 25, 26, 27, 28]   # Semana 2
    ]
]

ciudades = ["Tena", "Ibarra"]
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

# Calcular promedios por ciudad y semana
for i in range(len(temperaturas)):  # Iterar ciudades
    print(f"\nCiudad: {ciudades[i]}")
    for j in range(len(temperaturas[i])):  # Iterar semanas
        suma = 0
        contador = 0
        for k in range(len(temperaturas[i][j])):  # Iterar días
            suma += temperaturas[i][j][k]
            contador += 1
        promedio = suma / contador
        print(f"  Semana {j+1}: Promedio = {promedio:.2f}°C")
