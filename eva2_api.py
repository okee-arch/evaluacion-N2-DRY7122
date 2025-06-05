import requests

API_KEY = '5b3ce3597851110001cf62485621ae8498754c59b10a9800a47fd5b9'  

ciudades = {
    "santiago": [-70.6483, -33.4569],
    "ovalle": [-71.1983, -30.6017]
}

rendimiento_km_litro = 12  

print("Escribe 'q' para salir.\n")

while True:
    origen = input("Ciudad de origen (santiago/ovalle): ").lower()
    if origen == 'q':
        break
    destino = input("Ciudad de destino (santiago/ovalle): ").lower()
    if destino == 'q':
        break

    if origen not in ciudades or destino not in ciudades:
        print("Solo se permite 'santiago' y 'ovalle'")
        continue

    coords = [ciudades[origen], ciudades[destino]]
    url = "https://api.openrouteservice.org/v2/directions/driving-car/geojson"
    headers = {
        'Authorization': API_KEY,
        'Content-Type': 'application/json'
    }
    body = {
        "coordinates": coords,
        "language": "es"
    }

    try:
        response = requests.post(url, json=body, headers=headers)
        data = response.json()

        summary = data["features"][0]["properties"]["summary"]
        distancia_km = summary["distance"] / 1000
        duracion_min = summary["duration"] / 60
        combustible = distancia_km / rendimiento_km_litro

        print(f"\n Distancia: {distancia_km:.2f} km")
        print(f" Duración: {duracion_min:.2f} minutos")
        print(f" Combustible estimado: {combustible:.2f} litros\n")

        print(" Narrativa del viaje:")
        steps = data["features"][0]["properties"]["segments"][0]["steps"]
        for paso in steps:
            print(f"• {paso['instruction']}")

        print("\n--- Fin del recorrido ---\n")

    except Exception as e:
        print("Error al obtener datos:", e)
