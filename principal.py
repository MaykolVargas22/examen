import funciones as fn

trabajadores = ["Juan Pérez : ”,”María García”,”Carlos López”,”Ana Martínez”,”Pedro Rodríguez”,”Laura Hernández”,”Miguel Sánchez”,”Isabel Gómez”,”Francisco Díaz”,”Elena Fernández"]
sueldos_trabajadores = {}



while True:
    print("*****MENU*****")
    print("0. inicializar sueldos")
    print("1. asignar sueldos aleatorios")
    print("2. clasificar sueldos")
    print("3. ver estadisticas")
    print("4. reporte de sueldos")
    print("5. salir")

    opcion = int(input("ingrese su opcion"))

    if opcion == 0:
        sueldos_trabajadores = {trabajador : 0 for trabajador in trabajadores}
        print("sueldos inicializados correctamente")

    if opcion == 1:
        if not sueldos_trabajadores:
            print("primero debe inicializar los sueldos")
    else:
        sueldos_trabajadores = fn.asignar_sueldos_aleatorios(sueldos_trabajadores)

    
    
    if opcion == 2:
        if sueldos_trabajadores:
            fn.clasificar_sueldos(sueldos_trabajadores)
        else:
            print("primero debe inicializar sueldos")

    if opcion == 3:
        if sueldos_trabajadores:
            max_sueldo,min_sueldo,promedio_sueldo = fn.calcular_estadisticas(sueldos_trabajadores)
            if max_sueldo is not None:
                print("sueldo maximo: $",max_sueldo)
                print("sueldo minimo: ",min_sueldo)
                print("promedio sueldo: ",promedio_sueldo)
            else:
                print("primero debe asignar sueldos")


    elif opcion == 5:
        print("saliendo del programa...")

    
