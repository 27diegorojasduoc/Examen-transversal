from statistics import mean, geometric_mean
from random import randint

nombre = ["Juan Pérez","María García","Carlos López","Ana Martínez","Pedro Rodríguez", "Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]
sueldos = []
trabajadores = []

def sueldos_aleatorios():
    for trabajador in nombre:
        sueldos = {"nombre": trabajador} , {"sueldo": randint(300000, 2500000)}
        trabajadores.append(sueldos)
        print("Sueldos agregados con exito...")
        
def estadisticas():
    for i in trabajadores:
        print(f"El sueldo mas bajo es: {min(nombre)}")
        print(f"El sueldo mas alto es: {max(nombre)}")
    
        
                

    
while True:
    print("1)Asignar sueldos aleatorios")    
    print("2)Clasificar sueldos")    
    print("3)Ver estadisticas")    
    print("4)Reporte de sueldos")    
    print("5)Salir del programa")  
    opcion = input("Seleccione una opcion....  ")
    if opcion == "1":
        sueldos_aleatorios()
        
    elif opcion == "2":
        print(f"{trabajadores}")
    elif opcion == "3":
        estadisticas()
        print("Estadisticas")
        
    elif opcion =="4":
        print("Reporte de sueldos")
    elif opcion == "5":
        print("Finalizando programa... desarrollado por Diego Rojas, RUT 20.604.743-7")
        break
    else:
        print("Ingrese una opcion valida...")
        