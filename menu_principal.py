from Menu_empleado import main_empleado

def mostrar_menu():
    print("\n" + "*"*38)
    print("MENÚ PRINCIPAL".center(38))
    print("*"*38)
    print("""
    1. Gestionar Empleados
    2. Registrar Departamento (pendiente)
    3. Registrar Empleador (pendiente)
    4. Salir del sistema
    """)

def main():
    while True:
        mostrar_menu()
        try:
            opcion = int(input("Seleccione una opción: "))

            if opcion == 1:
                main_empleado()

            elif opcion == 2:
                print("Pendiente: Registar departamento")
            elif opcion == 3:
                print("Pendiente: Registrar Empleador")
            elif opcion == 4:
                print("Saliendo del sistema...")
                break
            else:
                print("Opción no válida. Intente de nuevo.")

        except ValueError:
            print("Por favor, ingrese una opción válida del menú.")

if __name__ == "__main__":
    main()