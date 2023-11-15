import mysql.connector
import sys

# Clase que implementa las operaciones con la BDD


class BDVideoJuegos:

    # constructor del objeto para conectar con la base de datos
    def __init__(self):
        self.bdconx = mysql.connector.connect(
            host="localhost",
            user="videojuegos",
            password="videojuegos",
            database="videojuegos")
    # fin de constructor

    def todosLosVideojuegos(self):
        # crear un cursor para hacer la consulta
        micursor = self.bdconx.cursor()

        # crear el texto de la consulta
        consulta = "SELECT * FROM videojuegosantiguos ORDER BY nombre"

        # ejecutar la consulta
        micursor.execute(consulta)

        # obtener las filas de la consulta y guardar en la variable
        miresultado = micursor.fetchall()

        # traza para ver el objeto miresultado
        sys.stderr.write(str(miresultado)+"\n")

        # cerrar cursor y conexion
        micursor.close()

        # Devolver resultados
        return miresultado

    def juegosConFiltro(self, filtro):
        # crear un cursor para hacer la consulta
        micursor = self.bdconx.cursor()

        # crear el texto de la consulta
        consulta = f"SELECT * FROM videojuegosantiguos {filtro} ORDER BY nombre"

        # ejecutar la consulta
        micursor.execute(consulta)

        # obtener las filas de la consulta y guardar en la variable
        miresultado = micursor.fetchall()

        # traza para ver el objeto miresultado
        sys.stderr.write(str(miresultado)+"\n")

        # cerrar cursor y conexion
        micursor.close()

        # Devolver resultados
        return miresultado

    def borrarPorId(self, id):
        # crear un cursor para hacer la consulta
        micursor = self.bdconx.cursor()

        # crear el texto de la consulta
        consulta = f"DELETE FROM videojuegosantiguos WHERE id = {id}"

        # ejecutar la consulta
        micursor.execute(consulta)

        self.bdconx.commit()

        # traza para ver el objeto miresultado
        sys.stderr.write(consulta+"\n")

        # cerrar cursor y conexion
        micursor.close()

    def insertar(self, nombre, empresa, tematica, numJug, anio):
        # crear un cursor para hacer la consulta
        micursor = self.bdconx.cursor()

        # crear el texto de la consulta
        consulta = "INSERT INTO videojuegosantiguos (nombre,empresa,tematica,numero_de_jugadores,publicacion) VALUES(%s, %s, %s, %s, %s)"
        val = (nombre, empresa, tematica, numJug, anio)

        # ejecutar la consulta
        micursor.execute(consulta, val)

        self.bdconx.commit()

        # traza para ver el objeto miresultado
        sys.stderr.write(consulta+"\n")

        # cerrar cursor y conexion
        micursor.close()

    def seleccionaPorId(self, id):
        # crear un cursor para hacer la consulta
        micursor = self.bdconx.cursor()

        # crear el texto de la consulta
        consulta = f"SELECT * FROM videojuegosantiguos WHERE id = {id}"

        # ejecutar la consulta
        micursor.execute(consulta)

        # recuperar la tupla con los datos buscados por el id
        miresultado = micursor.fetchone()

        # traza para ver el objeto miresultado
        sys.stderr.write(str(miresultado)+"\n")

        # cerrar cursor y conexion
        micursor.close()

        # Devolver resultados
        return miresultado

    def modificar(self, id, nombre, empresa, tematica, numJug, anio):
        #crear un cursor para hacer la consulta
        micursor = self.bdconx.cursor()


        #crear el texto de la consulta
        consulta = "UPDATE videojuegosantiguos SET nombre=%s,empresa=%s,tematica=%s,numero_de_jugadores=%s,publicacion=%s WHERE id=%s"
        sys.stderr.write(id)
        val = (nombre, empresa, tematica, int(numJug), int(anio), int(id))


        #ejecutar la consulta
        micursor.execute(consulta,val)


        self.bdconx.commit()


        #cerrar cursor y conexion
        micursor.close()


    def cerrarBD(self):
        self.bdconx.close()
