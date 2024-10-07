# Data access object - DAO
from flask import current_app as app
from app.conexion.Conexion import Conexion

class PaisDao:

    def getPaises(self):
        paisSQL = """
        SELECT id, nombre, apellido, pais
        FROM paises
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(paisSQL)
            # trae datos de la bd
            lista_paises = cur.fetchall()
            # retorno los datos
            lista_ordenada = []
            for item in lista_paises:
                lista_ordenada.append({
                    "id": item[0],
                    "nombre": item[1],
                    "apellido": item[2],
                    "pais": item[3]
                })
            return lista_ordenada
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

    def getPaisById(self, id):
        paisSQL = """
        SELECT id, nombre, apellido, pais
        FROM paises WHERE id=%s
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(paisSQL, (id,))
            # trae datos de la bd
            paisEncontrada = cur.fetchone()
            # retorno los datos
            return {
                "id": paisEncontrada[0],
                "nombre": paisEncontrada[1],
                "apellido": paisEncontrada[2],
                "pais": paisEncontrada[3]
            }
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

    def guardarPais(self, nombre, apellido, pais):
        insertPaisSQL = """
        INSERT INTO paises(nombre, apellido, pais) VALUES(%s, %s, %s)
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(insertPaisSQL, (nombre, apellido, pais))
            # se confirma la insercion
            con.commit()
            return True
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

        return False

    def updatePais(self, id, nombre, apellido, pais):
        updatePaisSQL = """
        UPDATE paises
        SET nombre=%s, apellido=%s, pais=%s
        WHERE id=%s
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(updatePaisSQL, (nombre, apellido, pais, id))
            # se confirma la actualizacion
            con.commit()
            return True
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

        return False

    def deletePais(self, id):
        deletePaisSQL = """
        DELETE FROM paises
        WHERE id=%s
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(deletePaisSQL, (id,))
            # se confirma la eliminación
            con.commit()
            return True
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

        return False
