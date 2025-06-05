# Evaluación N°2 DRY7122

## Nombre Asignatura
Programación y Redes Virtualizadas (SDN-NFV)

## Integrante
**Nombre del estudiante:** Rodrigo Gutiérrez  
**Fecha:** 5/6/2025

## Etapa A - Consumo de API Pública

Este script utiliza la API pública de [OpenRouteService](https://openrouteservice.org) para cumplir con los siguientes requerimientos:

###  Funcionalidades implementadas

- Solicita al usuario ingresar ciudad de origen y destino (Santiago/Ovalle)
- Realiza una consulta a la API de rutas (`/directions/driving-car/geojson`)
- Calcula:
  - Distancia total en kilómetros (2 decimales)
  - Duración del viaje (en minutos)
  - Estimación de combustible requerido (en litros)
- Imprime las instrucciones del viaje (narrativa), en español
- Permite salir del programa escribiendo `"q"`

###  Requisitos

- Python 3
- Módulo `requests` (instalar con `pip3 install requests --break-system-packages`)

###  Ejecución

```bash
python3 eva2_api.py
Prueba para activar pipeline
