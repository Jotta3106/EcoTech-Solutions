from DAO.CRUDEmpleado import CRUDEmpleado
from DAO.ConexionBD import ConexionBD
from DTO.EmpleadoDTO import EmpleadoDTO
from EcoTechMOO import Empleado

def main_empleado(conexion_bd=None):
    if conexion_bd is None:
        conexion_bd = ConexionBD()

    # Objeto de Acceso a Datos para manejar operaciones con el modelo Empleado
    dao_empleado = CRUDEmpleado(conexion_bd)

    while True:
        print("\n" + "*"*41)
        print("SUBMENÚ DE EMPLEADOS".center(41))
        print("*"*41)
        print("""
        1. Registrar empleado
        2. Listar empleados
        3. Buscar empleado
        4. Editar empleado
        5. Eliminar empleado
        6. Volver al menú principal
        """)

        try:
            opcion = int(input("Seleccione una opción: "))

            if opcion == 1:
                nombre = input("Nombre: ")
                apellido = input("Apellido:")
                direccion = input("Dirección: ")
                NumeroTelefono = input("Teléfono: ")
                correo = input("Correo:")
                password = input("Password:")
                inicioContrato = input("Inicio de contarto:")
                cod_departamento = input("Codigo de Departamento: ")

                # Creación objeto del dominio Empleado
                # codEmpleado no se solicita al crear un empleado aquí, usar None por defecto
                empleado = Empleado(nombre, apellido, direccion, NumeroTelefono, correo, password, None, inicioContrato, cod_departamento)

                # Creacion del DTO a partir del objeto del dominio
                empleado_dto = EmpleadoDTO(
                    nombre=empleado.nombre,
                    apellido=empleado.apellido,
                    direccion=empleado.direccion,
                    NumeroTelefono=empleado.NumeroTelefono,
                    correo=empleado.correo,
                    password=empleado.password,
                    codEmpleado=None,
                    inicioContrato=empleado.inicioContrato,
                    cod_departamento=empleado.codDepartamento
                )

                # Toma un objeto EmpleadoDTO, extrae sus datos y los guarda en una fila de la BD.
                dao_empleado.agregar(empleado_dto)

            elif opcion == 2:
                print("\n --- Lista de Empleadoos ---")
                lista_empleados = dao_empleado.mostrar_empleados()

                if not lista_empleados:
                    print("No hay empleados registrados. ")
                else: 
                    for empleado in lista_empleados:
                        print(f"ID_Empleado: {empleado.id_empleado}")
                        print(f"Nombre Completo: {empleado.nombre}, {empleado.apellido}")
                        print(f"Correo: {empleado.correo}")
                        print(f"Codigo Depatamento: {empleado.cod_departamento}")

            elif opcion == 3:
                cod_empleado = input("Ingrese el codigo del empleado que desea buscar:")
                empleado_encontrado = dao_empleado.buscar_empleado(cod_empleado)
                if empleado_encontrado:
                    print(f"Empleado encontrado: {empleado_encontrado}")
                else:
                    print("Empleado no encontrado.")

            elif opcion == 4:
                id_empleado = input("Ingrese el Codigo del empleado que desea editar: ")
                empleado_encontrado = dao_empleado.buscar_empleado(id_empleado)
                if empleado_encontrado:
                    print(f"Empleado encontrado: {empleado_encontrado}")
                    #Nuevos datos para ctualizar del empleado
                    nombre = input("Cambiar nombre")
                    apellido = input("Cambiar apellido")
                    direccion = input("Cambiar dirección")
                    NumeroTelefono = input("Cambiar teléfono")
                    correo = input("Cambiar correo")
                    password = input("Cambiar password")
                    inicioContrato = input("Cambiar inicio de contrato")
                    salario = input("Cambiar salario")

                #actualizamos el objeto mediante el DTO
                    empleado_encontrado.nombre = nombre
                    empleado_encontrado.apellido = apellido
                    empleado_encontrado.direccion = direccion
                    empleado_encontrado.NumeroTelefono = NumeroTelefono
                    empleado_encontrado.correo = correo
                    empleado_encontrado.password = password
                    empleado_encontrado.inicioContrato = inicioContrato
                    empleado_encontrado.Salrio = salario

                    dao_empleado.actualizar_empleado(empleado_encontrado)
                else:
                    print("Empleado no encointrado.")

            elif opcion == 5:
                id_empleado = input("Ingrese el Codigo del empleado que desea eliminar: ")
                empleado_encontrado = dao_empleado.buscar_empleado(id_empleado)
                if empleado_encontrado:
                    dao_empleado.eliminar_empleado(empleado_encontrado)

                else:
                    print("Empleado no encontrado.")

            elif opcion == 6:
                break

            else:
                print("Opción no válida. Elija un número del 1 al 6.")

        except ValueError:
            print("Entrada incorrecta. Por favor, ingrese un número para la opción.")

if __name__ == "__main__":
    main_empleado()