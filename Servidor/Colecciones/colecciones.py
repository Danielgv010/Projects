

# Listas
    # Cambiar items
        # list = ["apple","banana","cherry"]
        # list[1] = "blackcurrant"
        # Ahora la lista es ["apple","blackcurrant","cherry"]

        # list = ["apple","banana","cherry","orange","kiwi","mango"]
        # list[1:3] = ["blackcurrant","watermelon"]
        # Ahor la lista es ["apple","blackcurrant","watermelon","orange","kiwi","mango"]

        # list = ["apple", "banana", "cherry"]
        # list[1:2] = ["blackcurrant", "watermelon"]
        # Ahora la lista es ["apple","blackcurrant","watermelon","cherry"]

        # list = ["apple", "banana", "cherry"]
        # list[1:3] = ["watermelon"]
        # Ahora la lista es ["apple","watermelon"]

        # list = ["apple", "banana", "cherry"]
        # list.insert(2,"watermelon")
        # Ahora la lista es ["apple", "banana", "watermelon", "cherry"]

        # list = ["apple", "banana", "cherry"]
        # list.append("orange")
        # Ahora la lista es ["apple", "banana", "cherry","orange"]

        # list = ["apple", "banana", "cherry"]
        # second_list = ["mango", "pineapple", "papaya"]
        # list.extend(second_list)
        # Ahora la lista es ["apple", "banana", "cherry", "mango", "pineapple", "papaya"]
        # Funciona con cualquier iterable (tuplas, diccionarios, sets...)

    # Borrar items
        # list = ["apple", "banana", "cherry", "banana"]
        # list.remove("banana")
        # Ahora la lista es ["apple","cherry","banana"]

        # list = ["apple", "banana", "cherry"]
        # list.pop(1)
        # Ahora la lista es ["apple","cherry"]
        # Borra el elemento con idice especificado

        # list = ["apple", "banana", "cherry", "banana"]
        # list.pop()
        # Ahora la lista es ["apple","banana"]
        # Si no se especifica índice borra el último elemento

        # list = ["apple", "banana", "cherry"]
        # del list[0]
        # Ahora la lista es ["banana","cherry"]
        # Borra el elemento con idice especificado
        # del list    =>    Borra la lista entera

        # list = ["apple", "banana", "cherry"]
        # list.clear()
        # Ahora la lista es []

    # Ordenar la lista
        # list = [100, 50, 65, 82, 23]
        # list.sort(reverse = True)
        # Ahora la lista es [23,50,65,82,100]

        # list = [100, 50, 65, 82, 23]
        # list.sort(reverse = True)
        # Ahora la lista es [100,82,65,50,23]

        # Para ordenar según la cercanía del numero al 50
        # def myfunc(n):
        #     return abs(n - 50)
        # list = [100, 50, 65, 82, 23]
        # list.sort(key = myfunc)
        # Ahora la lista es [50,65,23,82,100]

        # Para ordenar una lista con strings sin que las mayusculas interfieran
        # list = ["apple", "Banana", "cherry"]
        # list.sort(key = str.lower)
        # Ahora la lista es ["banana","cherry"]

        # Para ordenar los resultados al revés
        # list = ["banana", "Orange", "Kiwi", "cherry"]
        # list.reverse()
        # Ahora la lista es ["cherry", "Kiwi", "Orange", "banana"]

    # Copiar listas
        # list = ["apple", "banana", "cherry"]
        # list_copy = list.copy()

        # list = ["apple", "banana", "cherry"]
        # list_copy = list(list)

    # Añadir elementos sets
        # set = {"apple", "banana", "cherry"}
        # set.add("orange")
        # Ahora el set es {"apple", "banana", "cherry", "orange"}

        # set = {"apple", "banana", "cherry"}
        # set2 = {"pinneaple", "mango", "papaya"}
        # set.update(set2)
        # Ahora el set es {"apple", "banana", "cherry", "pinneaple", "mango", "papaya"}
        # Funciona con cualquier iterable (tuplas, diccionarios, sets...)

    # Eliminar elementos sets
        # set = {"apple", "banana", "cherry"}
        # set.remove("banana")
        # Ahora el set es {"apple","cherry"}

        # set = {"apple", "banana", "cherry"}
        # set.discard("banana")
        # Ahora el set es {"apple","cherry"}

        # set = {"apple", "banana", "cherry"}
        # x = set.pop()
        # Elimina uno de los elementos aleatoriamente y lo devuelve

        # set = {"apple", "banana", "cherry"}
        # set.clear()
        # Ahora el set es {}

        # set = {"apple", "banana", "cherry"}
        # del set
        # Borra el set al completo

    # Unir sets
        # set1 = {"a", "b" , "c"}
        # set2 = {1, 2, 3}
        # set3 = set1.union(set2)
        # set3 ahora es {"a", "b" , "c", 1, 2, 3}

        # set1 = {"a", "b" , "c"}
        # set2 = {1, 2, 3}
        # set1.update(set2)
        # Ahora set1 es {"a", "b" , "c", 1, 2, 3}

        # x = {"apple", "banana", "cherry"}
        # y = {"google", "microsoft", "apple"}
        # x.intersection_update(y)
        # Ahora x es {"apple"} 

        # x = {"apple", "banana", "cherry"}
        # y = {"google", "microsoft", "apple"}
        # z = x.intersection(y)
        # Devuelve lo que coincida por lo que z es {"apple"}

        # x = {"apple", "banana", "cherry"}
        # y = {"google", "microsoft", "apple"}
        # x.symmetric_difference_update(y)
        # Ahora x es {"google", "banana", "microsoft", "cherry"}

        # x = {"apple", "banana", "cherry"}
        # y = {"google", "microsoft", "apple"}
        # z = x.symmetric_difference(y)
        # Devuelve lo que no coincida por lo que z es {"google", "banana", "microsoft", "cherry"}

    # Acceder al valor de un diccionario
        # thisdict = {"brand": "Ford","model": "Mustang","year": 1964}
        # x = thisdict["model"]
        # o también se puede usar
        # x = thisdict.get("model")

    # Actualizar el valor de un diccionario
        # thisdict = {"brand": "Ford","model": "Mustang","year": 1964}
        # thisdict["year"] = 2018
        # o también se puede usar
        # thisdict.update({year: 2018})
        # Si la clave no existe se crea un nuevo elemento con las dos formas

    # Eliminar valores de un diccionario
        # thisdict = {"brand": "Ford","model": "Mustang","year": 1964}
        # thisdict.pop("model")
        # Ahora el diccionario es {"brand": "Ford","year": 1964}
        # thisdict.popitem()
        # Elimina el último item insertado

        # thisdict = {"brand": "Ford","model": "Mustang","year": 1964}
        # del thisdict
        # Elimina el diccionario al completo

    # Recorrer diccionario
        # for x, y in thisdict.items():
        #   print(x, y)

    # Copiar un diccionario
        # dict1 = {"brand": "Ford","model": "Mustang","year": 1964}
        # dict2 = dict1.copy()
        # o también se puede usar
        # dict2 = dict(dict1)