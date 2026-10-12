from __future__ import annotations
from abc import ABC, abstractmethod
from datetime import date

#Parte de la Prueba jesus 
class Usuario(ABC):
    def __init__(self, Correo, password):
        self.correo = Correo
        # Expose password publicly for code that expects `password` attribute
        self.password = password
        self.__password = password 
    
    @abstractmethod
    def obtenerDatodos(self):
        pass

    
    def iniciarSesion(self, codEmpleado: int, Contraseña: str):
        if self.codEmpleado == codEmpleado and self.__contraseña == Contraseña:
            return "Inicio de Sesion Exitosa"
        return "Error al iniciar sesion, Intentalo Nuevamente"

class Empleado(Usuario): #Herencia de la clase usuario
    def __init__(self, nombre, apellido, direccion, NumeroTelefono, correo, contraseña, codEmpleado, inicioContrato, salario):
        super().__init__(correo, contraseña)
        self.nombre = nombre
        self.apellido = apellido
        self.direccion = direccion
        self.NumeroTelefono = NumeroTelefono
        self.codEmpleado = codEmpleado
        self.inicioContrato = inicioContrato
        self.Salario = salario 
        self.registroTiempo = []

    def obtenerDatodos(self):
        return f"Datos: {self.nombre} {self.apellido}, Codigo: {self.codEmpleado}"
    

    def registroHorasTrasbajadas(self,fecha: date, Horas: int):
        self.registroTiempo.append((fecha, Horas)) #agregacion de Horas trabajasas al registro del tiempo del empleado.

    def ingresarFecha(self, fecha: date): #Encapsulamiento de fecha ingresada por el empleado.
        self.fecha = fecha


    def ingresarTareas(self, tareas: str): #Encapsulamiento
        self.tareas = tareas
    

class RegistroTiempo():
    def __init__(self, fecha: date, horasTrabajadas: int):
        self.fecha = fecha
        self.horasTrabajadas = horasTrabajadas

    @abstractmethod
    def iniciarSesion(self, codEmpleado: int, password: str):
        if self.codEmpleado == codEmpleado and self.__password == password:
            return "Inicio de Sesion Exitosa"
        return "Error al iniciar sesion, Intentalo Nuevamente"

class Departamento():
    def __init__(self, nombre, codDepartamento, gerente):
        self.__nombre = nombre
        self.codDepartamento = codDepartamento
        self.gerente = gerente
        self.empleados = []

    def agregarEmpleado(self, empleado: Empleado): #Polimoprfismo
        self.empleados.append(empleado)
        return f"Empleado {empleado.nombre} {empleado.apellido} agregado al departamento {self.__nombre} con exito"
    

#Parte de Nico de la prueba 

class Proyecto():
    def __init__(self,nombre, codProyecto, descripcionProyecto,fechaInicio):
        self.nombre = nombre
        self.codproyecto = codProyecto
        self.descripcionproyecto = descripcionProyecto
        self.fechainicio = fechaInicio
        self.empleado  = []
        self.registrotiempo = []
        self.empleador = []

class Informe():
    def __init__(self,numInforme: int, formatoExportacion: str):
        self.numInforme = numInforme
        self.formatoExportacion = formatoExportacion
        self.empleador = []



#PARTE DE HECTOR
class Empleador(Usuario):
    def __init__(self, nombre, apellido, direccion, numero_telefono, correo, turno, password, cod_empleador, tareas):
        super().__init__(nombre, apellido, direccion, numero_telefono, correo, turno, password)
        self.cod_empleador = cod_empleador
        self.tareas = tareas
        self.informe = []
        self.departamento = []
        self.proyecto = []
        self.empleado = []

    def iniciar_sesion(self, cod_empleado: int, contraseña: str):
        if self.cod_empleado == cod_empleado and self.__password == contraseña:
            return "Inicio de sesion exitosa"
        return "Error al iniciar sesion, intentalo nuevamente"

    def registrar_nuevos_empleados(self, empleado: Empleado):
            self.empleado.append(empleado)
            return "Empleado registrado exitosamente"

    def generar_informes(self, informe: Informe):
                self.informe.append(informe)
                return "Informe generado exitosamente"

    def crear_departamento(self, departamento: Departamento):
            self.departamento.append(departamento)
            return "Departamento agregado exitosamente"

    def editar_departamentos(self, cod_departamento, nuevo_nombre = None, nuevo_gerente = None):
        for depa in self.departamento:
            if depa.cod_departamento == cod_departamento:
                if nuevo_nombre is not None:
                    depa.nombre = nuevo_nombre
                    print("Nombre modificado con éxito")
                if nuevo_gerente is not None:
                    depa.gerente = nuevo_gerente
                    print("Gerente modificado con éxito")

    def buscar_departamentos(self, codigo_depa):
        for depa in self.departamento:
            if depa.cod_departamento == codigo_depa:
                return "Los datos del departamento buscado son: {}".format(depa.mostrar_datos())
        return "Departamento no encontrado"

    def eliminar_departamentos(self, codigo_depa):
        for depa in self.departamentos:
            if depa.cod_departamento == codigo_depa:
                self.departamento.remove(depa)
                return "Departamento eliminado con exito"
        return "Departamento no encontrado"

    def asignar_empleado_depa(self, empleado: Empleado, nuevo_departamento: Departamento):
        empleado.departamento = nuevo_departamento

    def crear_proyectos(self, proyecto: Proyecto):
        self.proyecto.append(proyecto)
        return "Proyecto agregado exitosamente"

    def editar_proyectos(self, cod_proyecto, nuevo_nombre = None, nueva_desc = None):
        for pro in self.proyecto:
            if pro.cod_proyecto == cod_proyecto:
                if nuevo_nombre is not None:
                    pro.nombre = nuevo_nombre
                    print("Nombre modificado con éxito")
                if nueva_desc is not None:
                    pro.descripcion_proyecto = nueva_desc
                    print("Descripción modificada con éxito")
   
    def eliminar_proyecto(self, codigo):
        for pro in self.proyecto:
            if pro.cod_proyecto == codigo:
                self.proyecto.remove(pro)
                return "Proyecto eliminado con exito"
        return "Proyecto no encontrado"


    def mostrarInfoEmpleados(self,empleado: Empleado):
        print(f"Empleado: {empleado.nombre} {empleado.apellido} - Sueldo: {empleado.Salario}")

    def mostrarInfoProyectos(self, proyecto: Proyecto):
        print(f"Proyecto: {proyecto.nombre} - Código: {proyecto.codproyecto}")

    def mostrarInfoDepartamentos(self, departamento: Departamento):
         print(f"Departamento: {departamento.codDepartamento} - Gerente: {departamento.gerente} - Cantidad Empleados: {len(departamento.empleados)}")

    def mostrarRegistroTiempos(self, RegistroTiempo: int):
        print(f"Horas de {Empleado.nombre}: {Empleado.registroTiempo}")

#------------------------------------------------------------------------------------------------------------------------------------