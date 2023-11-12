
# Este python permite realizar varias operaciones sobre una base de datos
# Donde se pidan valores (filter_values, values, id) hay que pasarlos como lista

import mysql.connector, sys


class Database_Manager:


    # -------- Recibe como parámetros la IP donde está la BDD, el usuario con el que se pretende iniciar sesión en la BDD, su contraseña y el nombre de la BDD que se pretende usar --------

    def __init__(self, db_host, db_user, db_password, db_database): # Crea la conexión con la BDD basandose en los parametros que se pasan al constructor
        self.database_connection = mysql.connector.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            database=db_database)
    

    # -------- Recibe como parámetros el nombre de la tabla sobre la que hacer la consulta y el nombre de la columna sobre la que se ordenarán los resultados --------
    # -------- El parámetro order es opcional, si no se quiere ordenar se pone un 0 en su lugar --------

    def fetch_all(self, table, order): # Devuelve todos los registros de una tabla con el orden que se le indique
        db_cursor = self.database_connection.cursor() # Crea un cursor
        query = f"SELECT * FROM {table} "
        if order != 0: # Si el usuario pasó algo distinto a 0 en el parámetro order
            query += f"ORDER BY {order}"
        sys.stderr.write(str(query)+"\n") # Escribe la consulta completa en el log de errores de apache
        db_cursor.execute(query) # Ejecuta la consulta SQL
        result = db_cursor.fetchall() # Guarda los resultados de la consulta SQL en una variable
        db_cursor.close() # Cierra el cursor
        return result
    

    # -------- Recibe como parámetros el nombre de la tabla sobre la que hacer la consulta, el nombre de la columna sobre la que se ordenarán los resultados, --------
    # -------- un array con el nombre de las columnas sobre las que aplicar los filtros, un array con los filtros de dichas columnas y un boolean que permite --------
    # -------- indicar a la función si se está filtrando un valor unique como puede ser una clave primaria --------
    # -------- !!! No poner unique = True si el resultado trae multiples lineas !!! --------
    # -------- Solo sirve para filtrar con este formato ==> columna = valor --------

    def fetch_filtered(self, table, order, filter_columns, filter_values, unique): # Devuelve todos los registros de una tabla que coincidan con una serie de filtros
        iterator = 0
        db_cursor = self.database_connection.cursor() # Crea un cursor
        query = f"SELECT * FROM {table} WHERE "
        for column in filter_columns: # Por cada columna que se quiera filtrar se añade el filtro de la columna y si hay más filtros se añade AND
            iterator += 1
            query += column + " = %s "
            if iterator<len(filter_columns): # Si hay más filtros que añadir
                query += "AND "
        if order != 0: # Si se pasa algo distinto a 0 en el parámetro order se ordenan los resultados por ese parámetro
            query += f"ORDER BY {order}"
        sys.stderr.write(str(query)+"\n") # Escribe la consulta completa en el log de errores de apache
        db_cursor.execute(query,filter_values) # Ejecuta la consulta SQL rellenando los %s con las posiciones del array filter_values
        if unique: # Si se indica al metodo que el resultado es unico guarda solo un registro de la consulta
            result = db_cursor.fetchone() 
        else: # Si se indica al metod que el resultado no es unico, guarda todos los registros
            result = db_cursor.fetchall()
        db_cursor.close() # Cierra el cursor
        return result


    # -------- Recibe como parámetros el nombre de la taba sobre la que hacer la consulta, el filtro ya creado como string y los valores del filtro como un array --------

    def custom_query_fetch(self, table, custom_query, values): # Permite crear una consulta con un filtro más complejo a la bdd. Devuelve los registros que coincidan con el filtro
        db_cursor = self.database_connection.cursor() # Crea un cursor
        query = f"SELECT * FROM {table} WHERE {custom_query}"
        db_cursor.execute(query, values) # Ejecuta la consulta SQL rellenando los %s con las posiciones del array values
        result = db_cursor.fetchall() # Guarda todos los registros de la consulta en la variable
        sys.stderr.write(str(query)+"\n") # Escribe la consulta completa en el log de errores de apache
        db_cursor.close() # Cierra el cursor
        return result


    # -------- Recibe como parámetros el nombre de la taba sobre la que hacer el insert, el nombre de las columnas de la tabla como array y los valores de dichas columnas como array --------

    def insert(self, table, column_name, values): # Inserta un nuevo registro en la BDD
        iterator = 0
        db_cursor = self.database_connection.cursor() # Crea un cursor
        query = f"INSERT INTO {table} ("
        query_values = "" # Crea una variable donde meter la parte de VALUES() de la consulta SQL
        for name in column_name: # Por cada columna que se le haya pasado al metodo crea la parte del nombre de las columnas y la parte de valores en dos variables distintas simultáneamente
            iterator += 1
            query+=name
            query_values += "%s"
            if iterator<len(column_name): # Si hay más columnas que añadir añade una , a ambas partes de la sentencia SQL
                query += ", "
                query_values += ", "
        query += f") VALUES ({query_values})"
        sys.stderr.write(str(query)+"\n") # Escribe la consulta completa en el log de errores de apache
        db_cursor.execute(query,values) # Ejecuta la consulta SQL rellenando los %s con las posiciones del array values
        self.database_connection.commit() # Se aplican los cambios en la BDD
        db_cursor.close() # Cierra el cursor


    # -------- Recibe como parámetros el nombre de la tabla donde está el registro a borrar y el id de dicho registro -------- 

    def delete_with_id(self, table, id): # Borra un registro a partir de un id
        db_cursor = self.database_connection.cursor() # Crea un cursor
        query = f"DELETE FROM {table} " + "WHERE id = %s"
        sys.stderr.write(str(query)+"\n") # Escribe la consulta completa en el log de errores de apache
        db_cursor.execute(query, id) # Ejecuta la consulta SQL rellenando los %s con las posiciones del array id
        self.database_connection.commit() # Se aplican los cambios en la BDD
        db_cursor.close() # Cierra el cursor


    # -------- Recibe como parámetros el nombre de la tabla donde está el registro a modificar, el nombre de las columnas a modificar como array --------
    # -------- los nuevos valores de dichas columnas como array, el nombre de las columnas sobre las que aplicar un filtro como array y los valores --------
    # -------- de dichos filtros como array --------
    # -------- Los filtros son opcionales. Para hacer el cambio en todos los registros de la tabla, estos parámetros se pasan como 0 --------

    def modify(self, table, column_name, values, filter_columns, filter_values): # Modifica un registro de la BDD
        iterator = 0
        iterator2 = 0
        db_cursor = self.database_connection.cursor() # Crea un cursor
        query = f"UPDATE {table} SET "
        for name in column_name: # Por cada columna que se quiera modificar
            iterator += 1
            query += name + " = %s"
            if iterator<len(column_name): # Si hay más columnas que modificar
                query += ", "
        if filter_columns != 0: # Si se quiere hacer la modificación a unas columnas en específico
            query += " WHERE "
            for column in filter_columns: # Por cada columna que se quiera filtrar
                iterator2 += 1
                query += column + " = %s "
                if iterator2<len(filter_columns): # Si hay más filtros que añadir
                    query += "AND "
        sys.stderr.write(str(query)+"\n") # Escribe la consulta completa en el log de errores de apache
        db_cursor.execute(query,values+filter_values) # Ejecuta la consulta SQL rellenando los %s con las posiciones del array values y el array filter_values
        self.database_connection.commit() # Se aplican los cambios en la BDD
        db_cursor.close() # Cierra el cursor

    def close_database(self): # Cierra la BDD
        self.database_connection.close()