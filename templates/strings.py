
def split_letters(text): #Separa las letras en diferentes líneas
    for letter in text: # Por cada letra en el texto
        print(letter+"<br>")

def cuentaLetras(text): #Cuenta las letras de una frase sin contar los espacios o caracteres no alfanumericos
    counter = 0
    for letter in text.upper(): # Por cada letra del texto
        if letter >= "A" and letter <= "Z" or letter == "Ñ": # Si es una letra y no un caracter alfanumerico
            counter += 1 # El contador se incrementa en 1
    return counter # Devuelve el contador

def mirror_text(text): #Le da la vuelta al string
    return text[::-1] # Devuelve el string dado la vuelta


def contains_word(text,word): #Comprueba que la palabra envíada por el usuario esté en el texto que también envió
    return word in text  # Devuelve true o false

def count_letter(text,letter): #Devuelve el numero de veces que aparece la letra en el texto, en caso de error devuelve -1
    counter = 0
    if len(letter) == 1: # Si se le pasa una letra a la funcion
        for letter_iterator in text: # Por cada letra en el texto
            if (letter == letter_iterator): # Si la letra que se le pasa a la funcion es la misma que hay en el iterador de letras del texto
                counter += 1 # El contador se incrementa en 1
    else: # Si se le pasa algo distinto a 1 caracter
        counter = -1 # Contador -1
    return counter # Devuelve el contador

def count_vowels(text): #Centa cuantas vocales hay en el texto
    a=0
    e=0
    i=0
    o=0
    u=0
    for letter_iterator in text: # Por cada letra que haya en el texto
        match letter_iterator.lower(): # Switch de esa letra
            case "a": # Si es a
                a+=1
            case "e": # Si es e
                e+=1
            case "i": # Si es i
                i+=1
            case "o": # Si es o
                o+=1
            case "u": # Si es u
                u+=1
    return [a,e,i,o,u] # Devuelve un array con los contadores

def split_words(texto, separator): # Separa un texto por el separador que se le pasa a la funcion y lo devuelve como array
    return texto.split(separator)