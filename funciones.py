import random
import csv



def asignar_sueldos_aleatorios(trabajadores):

    sueldos_trabajadores = {}
    for trabajador in trabajadores:
        sueldo = random.randint(300000,2500000)
        sueldos_trabajadores[trabajador] = sueldo
    print("sueldos asignados correctamente")  
     
    print(sueldos_trabajadores)

    return sueldos_trabajadores


def clasificar_sueldos(sueldos_trabajadores):
    mayor_2500000 = {}
    menor_300000 = {}
    entre_300000_2500000 = {}
    for trabajador,sueldo in sueldos_trabajadores.items():
        if sueldo > 2500000:
            mayor_2500000[trabajador] = sueldo
        if sueldo < 300000:
            menor_300000[trabajador] = sueldo
        else:
            entre_300000_2500000[trabajador] = sueldo

    print("sueldo mayor a 2500000 TOTAL ",len(mayor_2500000))
    for trabajador,sueldo in mayor_2500000.items():
        print(trabajador, ": $",sueldo)    
    print("sueldo menor a 300000 TOTAL ",len(menor_300000))
    for trabajador,sueldo in menor_300000.items():
        print(trabajador, ": $",sueldo)       
    print("sueldo entre 300000 y 2500000 TOTAL ",len(entre_300000_2500000))
    for trabajador,sueldo in entre_300000_2500000.items():
        print(trabajador, ": $",sueldo)    



def calcular_estadisticas(sueldos_trabajadores):
    sueldos = list(sueldos_trabajadores.values())
    if not sueldos:
        print("no se han asignados sueldos aun")
        return None,None,None
    
    max_sueldo = max(sueldos)
    min_sueldo = min(sueldos)
    promedio_sueldo = sum(sueldos) / len(sueldos)
    return max_sueldo,min_sueldo,promedio_sueldo













        