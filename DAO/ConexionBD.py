from contextlib import contextmanager
import pymysql

class ConexionBD:
    def __init__(self, host="localhost", user="root", password="", db="ECOTECH_SOLUTIONS"):

        self.config = {
            "host": host,
            "user": user,
            "password": password,
            "db": db,
            # el auto commit se utiliza para
            "autocommit": False
        }
# El conetexmanagfer sirve para automatizar y asegurar ciclos de vida de nuestra base de datos.

    @contextmanager
    def obtener_conexion(self):
        #de esta manera se desempaqueta **  lo que generamos dentro de el self.config.
        conexionBD = pymysql.connect(**self.config)

        print("Conexio exitosa con la base de datos.\n")
        try:
            yield conexionBD # Entrega la conexion al metodo CRUD que lo invoca.
        except Exception:
            self.rollback(conexionBD)
            raise
        finally:
            self.desconectar(conexionBD)
# el sql es el que contiene string de la consulta y params son los parametros de una consulta.
    def ejecuta_query(self, conexionBD, sql, params=None):
        cursor = conexionBD.cursor()
        if params is None:
            cursor.execute(sql)
        else:
            cursor.execute(sql, params)
        return cursor

    def commit(self, conexionBD):
        conexionBD.commit()

    def rollback(self, conexionBD):
        conexionBD.rollback()

    def desconectar(self, conexionBD):
        conexionBD.close()
