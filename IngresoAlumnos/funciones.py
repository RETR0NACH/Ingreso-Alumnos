import random
import csv
trabajadores = [
    {"nombre": "Juan Pérez",},
    {"nombre": "María García", },
    {"nombre": "Carlos López", },
    {"nombre": "Ana Martínez", },
    {"nombre": "Pedro Rodríguez", },
    {"nombre": "Laura Hernández", },
    {"nombre": "Miguel Sánchez", },
    {"nombre": "Isabel Gómez", },
    {"nombre": "Francisco Díaz", },
    {"nombre": "Elena Fernández",}
]

import csv
import math 
# Asignación de sueldos aleatorios
sueldos = []

def asignar_sueldos_aleatorios():
    global sueldos #solo usamos el sueldo dentro de que está en este def
    sueldos = [random.randint(300000, 2500000) for _ in range(10)]
    print("Sueldos asignados aleatoriamente.")

def clasificar_sueldos(): #Se asignan los sueldos < $80000
    print("Sueldos menores a $800.000 TOTAL:", len([s for s in sueldos if s < 800000]))
    for trabajador, sueldo in zip(trabajadores, sueldos):
        if sueldo < 800000:
            print(f"Nombre empleado: {trabajador['nombre']}  Sueldo: ${sueldo}")
    #Asignamos los sueldos que sean entre $800.000 y $2.000.000
    print("\nSueldos entre $800.000 y $2.000.000 TOTAL:", len([s for s in sueldos if 800000 <= s <= 2000000]))
    for trabajador, sueldo in zip(trabajadores, sueldos):
        if 800000 <= sueldo <= 2000000:
            print(f"Nombre empleado: {trabajador['nombre']}  Sueldo: ${sueldo}")
    #Asignamos sueldos mayores a 2.000.000
    print("\nSueldos superiores a $2.000.000 TOTAL:", len([s for s in sueldos if s > 2000000]))
    for trabajador, sueldo in zip(trabajadores, sueldos):
        if sueldo > 2000000:
            print(f"Nombre empleado: {trabajador['nombre']}  Sueldo: ${sueldo}")
    #suma total de los sueldos de los empleados
    print("\nTOTAL SUELDOS:", sum(sueldos))

def ver_estadisticas():
    sueldo_max = max(sueldos) #sueldo maximo que tuvo un cliente
    sueldo_min = min(sueldos) #sueldo minimo del cliente
    sueldo_promedio = sum(sueldos) / len(sueldos) #promedio de sueldo maximo y mínimo


    print(f"Sueldo más alto: ${sueldo_max}")
    print(f"Sueldo más bajo: ${sueldo_min}")
    print(f"Promedio de sueldos: ${sueldo_promedio:.2f}")


def reporte_sueldos():
    with open('reporte_sueldos.csv', 'w', encoding='utf-8' ,newline='') as archivo:
        archivo = csv.writer(archivo)
        archivo.writerow(["NOMBRE EMPLEADO", "SUELDO BASE", "DESCUENTO SALUD", "DESCUENTO AFP", "SUELDO LIQUIDO"])
        for trabajador, sueldo in zip(trabajadores, sueldos):
            descuento_salud = sueldo * 0.07
            descuento_afp = sueldo * 0.12
            sueldo_liquido = sueldo - descuento_salud - descuento_afp
            archivo.writerow([trabajador["nombre"], trabajador, sueldo, descuento_salud, descuento_afp, sueldo_liquido])
            print(f"NOMBRE EMPLEADO: {trabajador['nombre']}  SUELDO BASE: ${sueldo} DESCUENTO SALUD: ${descuento_salud:.2f} DESCUENTO AFP: ${descuento_afp:.2f} SUELDO LIQUIDO: ${sueldo_liquido:.2f}")
