ids = []
empleados = []
cargos = []
sueldos = []
fechas = []
motivos = []
observaciones = []
#-----------------------------------------#
#--|menu_principal_ajustador_de_sueldos|--#
#-----------------------------------------#
while True:
    print("menu principal ajustador de sueldos")
    print("1) crear sueldo")
    print("2) editar sueldo")
    print("3) eliminar sueldo")
    print("4) buscar sueldo")
    print("5) lista de datos")
    print("6) salir")
    opcion = input("seleccione una opción: ")
    #------------------#
    #--|crear_sueldo|--#
    #------------------#
    if opcion == "1":
        if len(ids) == 0:
            id_sueldo = 1
        else:
            id_sueldo = ids[-1] + 1
        empleado = input("nombre del empleado: ")
        cargo = input("cargo: ")
        sueldo = float(input("sueldo: "))
        fecha = input("fecha del ajuste: ")
        motivo = input("motivo del ajuste: ")
        observacion = input("observación: ")
        ids.append(id_sueldo)
        empleados.append(empleado)
        cargos.append(cargo)
        sueldos.append(sueldo)
        fechas.append(fecha)
        motivos.append(motivo)
        observaciones.append(observacion)
        print("sueldo registrado correctamente.")
        print("id:", id_sueldo)
    #-------------------#
    #--|editar_sueldo|--#
    #-------------------#
    elif opcion == "2":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            print("editar sueldo")
            for i in range(len(ids)):
                print(f"{ids[i]} | {empleados[i]} | {cargos[i]} | {sueldos[i]} | {fechas[i]} | {motivos[i]} | {observaciones[i]}")
            id_buscar = int(input("ingrese la id del registro: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos actuales")
                print(f"{ids[posicion]} | {empleados[posicion]} | {cargos[posicion]} | {sueldos[posicion]} | {fechas[posicion]} | {motivos[posicion]} | {observaciones[posicion]}")
                empleados[posicion] = input("nuevo nombre del empleado: ")
                cargos[posicion] = input("nuevo cargo: ")
                sueldos[posicion] = float(input("nuevo sueldo: "))
                fechas[posicion] = input("nueva fecha del ajuste: ")
                motivos[posicion] = input("nuevo motivo del ajuste: ")
                observaciones[posicion] = input("nueva observación: ")
                print("registro actualizado correctamente.")
            else:
                print("id no encontrada.")
    #---------------------#
    #--|eliminar_sueldo|--#
    #---------------------#
    elif opcion == "3":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            print("eliminar sueldo")
            for i in range(len(ids)):
                print(f"{ids[i]} | {empleados[i]} | {cargos[i]} | {sueldos[i]} | {fechas[i]} | {motivos[i]} | {observaciones[i]}")
            id_buscar = int(input("ingrese la id del registro: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos del registro")
                print(f"{ids[posicion]} | {empleados[posicion]} | {cargos[posicion]} | {sueldos[posicion]} | {fechas[posicion]} | {motivos[posicion]} | {observaciones[posicion]}")
                respuesta = input("¿desea eliminar este registro? (s/n): ")
                if respuesta.upper() == "S":
                    ids.pop(posicion)
                    empleados.pop(posicion)
                    cargos.pop(posicion)
                    sueldos.pop(posicion)
                    fechas.pop(posicion)
                    motivos.pop(posicion)
                    observaciones.pop(posicion)
                    print("registro eliminado correctamente.")
                else:
                    print("el registro no fue eliminado.")
            else:
                print("id no encontrada.")
    #-------------------#
    #--|buscar_sueldo|--#
    #-------------------#
    elif opcion == "4":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            print("buscar sueldo")
            id_buscar = int(input("ingrese la id del registro: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos del registro")
                print(f"{ids[posicion]} | {empleados[posicion]} | {cargos[posicion]} | {sueldos[posicion]} | {fechas[posicion]} | {motivos[posicion]} | {observaciones[posicion]}")
            else:
                print("id no encontrada.")
    #-----------------#
    #--|lista_datos|--#
    #-----------------#
    elif opcion == "5":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            suma = 0
            mayor = sueldos[0]
            menor = sueldos[0]
            print("lista de datos")
            for i in range(len(ids)):
                print(f"{ids[i]} | {empleados[i]} | {cargos[i]} | {sueldos[i]} | {fechas[i]} | {motivos[i]} | {observaciones[i]}")
                suma += sueldos[i]
                if sueldos[i] > mayor:
                    mayor = sueldos[i]
                if sueldos[i] < menor:
                    menor = sueldos[i]
            promedio = suma / len(ids)
            print("estadísticas ajustador de sueldos")
            print("cantidad de empleados:", len(ids))
            print("total de sueldos: $", round(suma, 2))
            print("sueldo promedio: $", round(promedio, 2))
            print("sueldo más alto: $", round(mayor, 2))
            print("sueldo más bajo: $", round(menor, 2))
    #------------------------------#
    #--|salir_del_menu_principal|--#
    #------------------------------#
    elif opcion == "6":
        print("gracias por utilizar el ajustador de sueldos.")
        break
    else:
        print("opción no válida.")