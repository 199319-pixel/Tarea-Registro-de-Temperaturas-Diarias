from typing import List, Dict, Optional

def calcular_promedios(
    temperaturas: List[List[List[float]]],
    ciudades: List[str]
) -> Dict[str, Optional[float]]:
    """
    Calcula el promedio de temperatura POR CIUDAD para todo el período.
    - temperaturas: lista 3D [ciudad][semana][día]
    - ciudades: lista de nombres de ciudades, misma longitud que temperaturas
    Retorna: dict {ciudad: promedio} (None si no hay datos para la ciudad)
    """
    if len(temperaturas) != len(ciudades):
        raise ValueError("La longitud de 'temperaturas' debe coincidir con 'ciudades'.")

    resultados: Dict[str, Optional[float]] = {}
    for i, ciudad in enumerate(ciudades):
        suma_total = 0.0
        dias_total = 0
        # Recorremos semanas y días
        for semana in temperaturas[i]:
            if not isinstance(semana, list):
                raise ValueError("Cada 'semana' debe ser una lista de temperaturas diarias.")
            for temp in semana:
                # Convertir a float por seguridad (acepta int o float)
                suma_total += float(temp)
                dias_total += 1
        # Si no hubo días para esa ciudad, guardamos None
        resultados[ciudad] = (suma_total / dias_total) if dias_total else None
    return resultados


# -------------- Bloque de prueba / ejemplo --------------
if __name__ == "__main__":
    # Datos de ejemplo: 3 ciudades, 4 semanas, 7 días por semana
    temperaturas = [
        [   # Ibarra
            [30, 31, 29, 28, 32, 33, 30],
            [29, 28, 27, 30, 31, 32, 33],
            [25, 26, 27, 28, 29, 30, 31],
            [32, 33, 34, 30, 29, 28, 27]
        ],
        [   # Tena
            [25, 26, 27, 28, 29, 30, 31],
            [28, 27, 29, 30, 32, 31, 33],
            [30, 31, 29, 28, 27, 26, 25],
            [32, 33, 31, 30, 29, 28, 27]
        ],
        [   # Quito
            [18, 19, 20, 21, 22, 23, 24],
            [20, 21, 22, 23, 24, 25, 26],
            [22, 21, 20, 19, 18, 17, 16],
            [19, 20, 21, 22, 23, 24, 25]
        ]
    ]
    ciudades = ["Ibarra", "Tena", "Quito"]

    resultados = calcular_promedios(temperaturas, ciudades)

    print("Promedio de temperaturas por ciudad:\n")
    for ciudad, promedio in resultados.items():
        if promedio is None:
            print(f"{ciudad}: no hay datos.")
        else:
            print(f"{ciudad}: {promedio:.2f}°C")
