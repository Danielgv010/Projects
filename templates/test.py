#!C:\Users\deras\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\python.exe

import cookies, database, cgiloader

# print("Content-type: text/html\n")
# cookies.create_cookie("testa","1","Mon, 13 Nov 2023 07:30:00 GMT;")
# cookies.counter_cookie("testa","-")
# cookies.counter_cookie("testa","+")
# cookies.delete_cookie("test")
# cookies.update_cookie("test","test2","Mon, 13 Nov 2023 07:30:00 GMT;")
# cookies.update_cookie_expiration("test", "Tue, 14 Nov 2023 07:30:00 GMT;")
# print(cookies.check_cookie_existence("test"))
# print(cookies.get_cookie_value("test"))


# print("Content-type: text/html\n")
# db = database.Database_Manager("localhost","test","test","test")

# print(db.fetch_all("test","country"))

# Comprobar que funciona el que muestre solo una linea
# filter_column = ["id","age"]
# filter_value = ["1","1"]
# print(db.fetch_filtered("test","id",filter_column, filter_value, True))

# column_name = ["name", "age", "country"]
# values = ["lolo", "20", "spain"]
# db.insert("test",column_name, values)

# db.delete_with_id("test",["4"])

# column_name = ["age","country"]
# values = ["1","finland"]
# filter_columns = ["name","country"]
# filter_values = ["pepe","spain"]
# db.modify("test",column_name,values,filter_columns,filter_values)

# db.close_database()

# cgiloader.save_file("test-upload","files/")
# print(cgiloader.create_table("files/","ligafutbol.csv",";"))

# original_array = [1, 2, 3, 4, 5]
# second_array = original_array[1:4]

# print(second_array)

tuple = (1,2,3,4)
array = [1,2,3,4]
diccionario = {"uno":1,"dos":2}
set = {1,2,3,4}

print(help(set))
# print(diccionario.get("dos"))
# print(diccionario.items())
# print(diccionario.keys())
# print(diccionario.values())
