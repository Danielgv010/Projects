import mysql.connector
import sys

class DBmanager:
    def __init__(self):
        self.bdconx = mysql.connector.connect(
            host='localhost',
            user='videojuegos',
            password='videojuegos',
            database='videojuegos')
        
    def list_all(self):
        # crear un cursor para hacer la consulta
        my_cursor = self.bdconx.cursor()

        # crear el texto de la consulta
        query = 'SELECT * FROM videojuegosantiguos ORDER BY nombre'

        # ejecutar la consulta
        my_cursor.execute(query)

        # obtener las filas de la consulta y guardar en la variable
        result = my_cursor.fetchall()

        # traza para ver el objeto miresultado
        sys.stderr.write(str(result)+'\n')

        # cerrar cursor y conexion
        my_cursor.close()

        # Devolver resultados
        return result
    
    def insert_row(self,name,company,theme,player_count,release_date):
        # crear un cursor para hacer la consulta
        my_cursor = self.bdconx.cursor()

        # crear el texto de la consulta
        query='INSERT INTO videojuegosantiguos (nombre,empresa,tematica,numero_de_jugadores,año_de_publicacion) VALUES(%s, %s, %s, %s, %s)'
        values = (name,company,theme,player_count,release_date)
        # ejecutar la consulta

        my_cursor.execute(query, values)

        self.bdconx.commit()

        # traza para ver el objeto miresultado
        sys.stderr.write(query+"\n")

        # cerrar cursor y conexion
        my_cursor.close()

    def delete(self, id):
        # crear un cursor para hacer la consulta
        my_cursor = self.bdconx.cursor()

        # crear el texto de la consulta
        query=f'DELETE FROM videojuegosantiguos WHERE id = {id}'
        # ejecutar la consulta

        my_cursor.execute(query)

        self.bdconx.commit()

        # traza para ver el objeto miresultado
        sys.stderr.write(query+"\n")

        # cerrar cursor y conexion
        my_cursor.close()

        
    def close_database(self):
        self.bdconx.close()