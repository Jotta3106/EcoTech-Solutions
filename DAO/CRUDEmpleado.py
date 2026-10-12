from DTO.EmpleadoDTO import EmpleadoDTO
from DAO.ConexionBD import ConexionBD
import pymysql

class CRUDEmpleado:
    def __init__(self, conexion: ConexionBD):
        if conexion is None:
            raise ValueError("CRUDEmpleado necesita de una conexion existente")
        self.conexion = conexion

    def agregar(self, empleado_dto: EmpleadoDTO):
        return self.AgregarEmpleado(empleado_dto)

    def AgregarEmpleado(self, empleado_dto: EmpleadoDTO):
        try:
            with self.conexion.obtener_conexion() as conexion_activa:
                #sacar codigo empleado debido a que este es generado de manera automatica 
                
                cursor = self.conexion.ejecuta_query(conexion_activa, """
                    INSERT INTO Empleado (nombre, apellido, direccion, numero_telefono, correo, turno, password, cod_departamento) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                """, (
                    empleado_dto.nombre,
                    empleado_dto.apellido,
                    empleado_dto.direccion,
                    empleado_dto.NumeroTelefono,
                    empleado_dto.correo,
                    empleado_dto.turno,
                    empleado_dto.password,
                    empleado_dto.cod_departamento
                ))
                #El CRUD interactua y  confirma el cambio exitoso.
                self.conexion.commit(conexion_activa)
                empleado_dto.cod_empleado = cursor.lastrowid
            print("Empleado Agregado Exitosamente")
            return empleado_dto
        except Exception as e:
            print("Error al agregar al empleado a la Base de Datos", e)
            return None

    def mostrar_empleados(self):
        try:
            with self.conexion.obtener_conexion() as conexion_activa:
                cursor = self.conexion.ejecuta_query(
                    conexion_activa,
                    "SELECT * FROM Empleado"
                )

                filas = cursor.fetchall()
                return [
                    EmpleadoDTO(
                        codEmpleado=fila[0],
                        nombre=fila[1],
                        apellido=fila[2],
                        direccion=fila[3],
                        NumeroTelefono=fila[4],
                        correo=fila[5],
                        password=fila[7],
                        turno=fila[6],
                        cod_departamento=fila[8]
                    )
                    for fila in filas
                ]
        except pymysql.MySQLError as e:
            print("Error al mostrar los empkleados de la Base de Datos", e)
            return[]
#--------------------------------------------------------------------------------------------

    def actualizar_empleado(self, empleado_dto: EmpleadoDTO):
        """Actualiza los datos de un empleado existente utilizando su cod_empleado."""
        try:
            with self.conexion.obtener_conexion() as conexion_activa:
                query = """
                    UPDATE Empleado 
                    SET nombre = %s, apellido = %s, direccion = %s, nuemero_telefono = %s, 
                        correo = %s, tueno = %s, password = %s, cod_departamento = %s
                    WHERE cod_Empleado = %s
                """
                valores = (
                    empleado_dto.nombre,
                    empleado_dto.apellido,
                    empleado_dto.direccion,
                    empleado_dto.numero_telefono,
                    empleado_dto.correo,
                    empleado_dto.turno,
                    empleado_dto.password,
                    empleado_dto.cod_departamento,
                    empleado_dto.cod_empleado  # El identificador para el WHERE
                )
                
                cursor = self.conexion.ejecuta_query(conexion_activa, query, valores)
                self.conexion.commit(conexion_activa)
                
                # Verificamos si realmente se modificó alguna fila
                if cursor.rowcount > 0:
                    print(f"Empleado con código {empleado_dto.cod_empleado} actualizado exitosamente.")
                    return True
                else:
                    print(f"No se encontró ningún empleado con el código {empleado_dto.cod_empleado}.")
                    return False
        except Exception as e:
            print("Error al actualizar el empleado en la Base de Datos:", e)
            return False

    # CONTINUACIÓN DEL CRUD: Método Eliminar (Delete)
    def eliminar_empleado(self, cod_empleado: int):
        """Elimina un empleado de la base de datos mediante su código identificador."""
        try:
            with self.conexion.obtener_conexion() as conexion_activa:
                query = "DELETE FROM Empleado WHERE cod_Empleado = %s"
                
                cursor = self.conexion.ejecuta_query(conexion_activa, query, (cod_empleado,))
                self.conexion.commit(conexion_activa)
                
                if cursor.rowcount > 0:
                    print(f"Empleado con código {cod_empleado} eliminado exitosamente.")
                    return True
                else:
                    print(f"No se encontró ningún empleado con el código {cod_empleado} para eliminar.")
                    return False
        except Exception as e:
            print("Error al eliminar el empleado de la Base de Datos:", e)
            return False
        