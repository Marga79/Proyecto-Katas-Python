# %%
# 1. Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias
# de cada letra en la cadena. Los espacios no deben ser considerados.
# Esto es crear una función que cuente la frecuencia de cada letra en una cadena.

def contar_letras(cadena_texto):
    
    frecuencias = {}

    for letra in cadena_texto:
        if letra == ' ':
            continue
        if letra in frecuencias:
            frecuencias[letra] += 1
        else:
            frecuencias[letra] = 1

    return frecuencias

## defino la variable que contiene el texto:
texto = "Tengo una mascota"
resultado = contar_letras(texto)
print(resultado)

# %%
print(f"la frecuencia de cada letra del texto es: = {resultado}")

# %%
## 2. Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map()

# mi lista de numeros:
numeros = [1, 2, 3, 4, 5, 6, 7]
# defino la funcion que da el doble del valor inicial:
dobles = list(map(lambda x: x * 2, numeros))

# %%
print(dobles)

# %%
##3. Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros.
# La función debe devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.
def lista_de_palabras(lista_palabras, palabra_objetivo):
   
    lista_definitiva = []

    for palabra in lista_palabras:

        if palabra_objetivo in palabra:
            lista_definitiva.append(palabra)
            
    return lista_definitiva


# %%
palabras = ["ratón", "perro", "murcielago", "oveja", "leon"]
objetivo = "lago"
resultado = lista_de_palabras(palabras, objetivo)

print(f"La lista de palabras es: {palabras}")
print(f"La palabra objetivo es: {objetivo}")
print(f"Palabras que contienen la palabra objetivo es: {resultado}")


# %%
## 4.	Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map()

def calcular_diferencia(lista1, lista2):
    """
    Calcula la diferencia entre los valores de dos listas usando map().
    Resta cada elemento de lista2 del elemento correspondiente de lista1.
    
    Args:
        lista1 (list): Primera lista de números
        lista2 (list): Segunda lista de números
    
    Returns:
        list: Lista con las diferencias (lista1 - lista2)
    """
    return list(map(lambda x, y: x - y, lista1, lista2))

# %%
lista_a = [2, 20, 50, 100]
lista_b = [2, 5, 10, 25]
diferencias = calcular_diferencia(lista_a, lista_b)

# %%
print(f"La lista resultante es: {diferencias}")

# %%
## 5. Escribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por defecto es 5. 
## La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual que la nota aprobado. 
## Si es así, el estado será "aprobado", de lo contrario, será "suspenso". La función debe devolver una tupla que contenga la media y el estado.

def calcular_media(lista_numeros, nota_aprobado=5):
    """ defino la funcion que calcula la media de la lista de numeros e indica si es suspenso o aprobado en funcion de la nota

    Args:
        lista_numeros (list): lista de numeros
        nota_aprobado (int, optional): nota aprobado
    Returns:
        tupla:(media, estado)

    """
# defino la media y hago el bucle
    media = sum(lista_numeros) / len(lista_numeros)

    if media >= nota_aprobado:
        estado = "aprobado"
    else:
        estado = "suspenso"
    
    return (media, estado)

# %%
numeros = [3, 5, 6, 8, 1, 2, 8, 9, 10, 4]
resultado = calcular_media(numeros,5)

# %%
print(resultado)

# %%
## 6.	Escribe una función que calcule el factorial de un número de manera recursiva.

def factorial(numero):
    """
    Calcula el factorial de un número de manera recursiva.
    
    El factorial del numero n (n!) es el producto de todos los números enteros 
    positivos desde 1 hasta n.
    
    Args:
        numero (int): Número entero no negativo
    
    Returns:
        int: El factorial de n
    """
    # Caso base: 0! = 1 y 1! = 1
    if numero == 0 or numero == 1:
        return 1
    
    # Caso recursivo: n! = n * (n-1)!
    return numero * factorial(numero - 1)

# %%
numeros = [0, 1, 2, 3, 4, 5, 6, 7]
for num in numeros:
    resultado = factorial(num)
    print(f"{num}! = {resultado}")

# %%
## 7. Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map()

def tuplas_a_strings(lista_tuplas):
    """
    Convierte una lista de tuplas a una lista de strings.
    
    Args:
        lista_tuplas (list): Lista de tuplas que quiero convertir
        
    Returns:
        list: Lista de strings
    """
    return list(map(str, lista_tuplas))

# %%
tuplas_numeros = [(1, 2), (3, 4), (5, 6)] 

resultado = tuplas_a_strings(tuplas_numeros)

# %%
print(f"Lista de strings: {resultado}")
print(type(resultado[0]))

# %%
## 8. Escribe un programa que pida al usuario dos números e intente dividirlos.
# Si el usuario ingresa un valor no numérico o intenta dividir por cero, maneja esas excepciones de manera adecuada.
# Asegúrate de mostrar un mensaje indicando si la división fue exitosa o no.

def division():
    try:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        resultado = num1 / num2
    except ValueError:
        print("Error: Debes ingresar valores numéricos")
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero")
    else:
        print(f"El valor de la división de {num1} entre {num2} es: {resultado}")

division()

# %%
## 9. Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista excluyendo 
## ciertas mascotas prohibidas en España.
## La lista de mascotas a excluir es ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]. Usa la función filter()


def mascotas_permitidas(lista_mascotas):
    """Función que toma una lista de mascotas y devuelve una nueva lista excluyendo las mascotas prohibidas en España

    Args:
        lista_mascotas (list): Lista con nombres de mascotas

    Returns:
        lista: una lista solo con las mascotas permitidas en España
    """

    prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]
    
    # Usamos filter para excluir las mascotas prohibidas
    mascotas = filter(lambda mascota: mascota not in prohibidas, lista_mascotas)
    
    return list(mascotas)

# %%
lista = ["Perro", "Gato", "Mapache", "León", "Pájaro"]
resultado = mascotas_permitidas(lista)
print(resultado)  

# %%
print("Mascotas permitidas:", resultado)


# %%
## 10. Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una
##    excepción personalizada y maneja el error adecuadamente.

class ListaVaciaError(Exception):
    """Excepción personalizada para listas vacías."""
    pass

def calcular_promedio(numeros):
    if not numeros:
        raise ListaVaciaError("La lista de números está vacía. No se puede calcular el promedio.")
    return sum(numeros) / len(numeros)

# Manejo del error
try:
    lista = []  
    promedio = calcular_promedio(lista)
    print(f"El promedio es: {promedio}")
except ListaVaciaError as e:
    print(f"Error: {e}")

# %%
## 11. Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un
## valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones adecuadamente.

class Error_Edad(Exception):
    pass
## introducimos la edad con un input
try:
    entrada = input("Introduce tu edad: ")
    edad = int(entrada)  # Puede lanzar ValueError

    if edad < 0 or edad > 120:
        raise Error_Edad("La edad debe estar comprendida entre 0 y 120 años")
    
    print(f"La edad es: {edad}")

except ValueError:
    print("Error: La entrada no es un número válido")
except Error_Edad as e:
    print(f"Error: {e}")

# %%
## 12. Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la función map()

def longitud_de_las_palabras(frase):
    """esta función calcula la longitud de cada palabra de la frase dada

    Args:
        frase (texto): La frase dada

    Returns:
        _lista: lista con la longitud de cada palabra de la frase dada
    """
    palabras = frase.split() # divide la frase en cada una de las palabras que contiene
    longitudes = list(map(len, palabras)) # aplica la función len() a cada palabra y ese resultado lo convierte en una lista que se llama "longitudes"
    return longitudes

frase = "Me está resultando muy difícil estudiar Python"
print(longitud_de_las_palabras(frase))

# %%
## 13. Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en
##     mayúsculas y minúsculas. Las letras no pueden estar repetidas. Usa la función map()

def mayus_minus_letras(caracteres):
    """Función que nos da una lista de tuplas con cada letra única en mayúscula y minúscula de un texto determinado.

    Args:
        caracteres (_str): texto (conjunto de caracteres de tipo string, en este caso)

    Returns:
        lista: Lista de tuplas, donde cada tupla contiene la mayúscula y la minúscula de cada letra del texto
    """
    letras_vistas = set()
    letras_unicas = []

    for c in caracteres:
        clave = c.lower()
        if clave not in letras_vistas:
            letras_vistas.add(clave)
            letras_unicas.append(c)
            
    resultado = list(map(lambda c: (c.upper(), c.lower()), letras_unicas))
    return resultado


# %%
entrada = "Hola"
print(mayus_minus_letras(entrada))

# %%
## 14. Crea una función que retorne las palabras de una lista de palabras que comience con una letra en especifico. Usa la función filter()

def palabras_con_letra_especifica(palabras, letra):
    """Función que nos da las palabras que comienzan con una letra específica dada

    Args:
        palabras (_lista): lista de palabras
        letra (str): letra de tipo string que será la letra clave que devuelva

    Returns:
        _lista: lista de palabras que contengan la letra dada
    """
    return list(filter(lambda palabra: palabra.startswith(letra), palabras))


# %%
lista = ["uvas", "melón", "pera", "sandía", "albaricoque", "mango", "manzana"]
print(palabras_con_letra_especifica(lista, "m"))

# %%
## 15. Crea una función lambda que sume 3 a cada número de una lista dada.

sumar_tres = lambda lista: list(map(lambda x: x + 3, lista))

numeros = [4, 25, 11, 108]
print(sumar_tres(numeros))

# %%
## 16. Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de
##     todas las palabras que sean más largas que n. Usa la función filter()

def palabras_mas_largas_que_n(texto, n):
    """
    Función que toma una cadena de texto y un número entero n como parámetros
    y devuelve una lista de todas las palabras que sean más largas que n.
    
    Args:
        texto (str): La cadena de texto a procesar
        n (int): La longitud mínima que deben tener las palabras
    
    Returns:
        list: Lista de palabras que son más largas que n
    """
    # Divide el texto en palabras
    palabras = texto.split()
    
    # Usar filter() para obtener solo las palabras más largas que n
    palabras_filtradas = filter(lambda palabra: len(palabra) > n, palabras)
    
    # Convierte el resultado a lista
    return list(palabras_filtradas)

# %%
texto = "Estudiar Python me resulta muy difícil"
n = 7
resultado = palabras_mas_largas_que_n(texto, n)

# %%
print(f"Las palabras con más de 7 caracteres son: {resultado}")

# %%
## 17. Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, [5,7,2]
##     corresponde al número quinientos setenta y dos (572). Usa la función reduce()

from functools import reduce ## tengo que importar la funcion de la libreria

def lista_a_numero(digitos):
    return reduce(lambda x, y: x * 10 + y, digitos)

resultado = lista_a_numero([5, 7, 2])
print(resultado)  # Muestra: 572

# %%
## 18. Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes (nombre, edad, calificación)
#  y use la función filter para extraer a los estudiantes con una calificación mayor o igual a 90. Usa la función filter()

# Creamos la lista de diccionarios con información de los estudiantes
estudiantes = [
    {"nombre": "Ana", "edad": 18, "calificacion": 90},
    {"nombre": "María", "edad": 22, "calificacion": 80},
    {"nombre": "Marcos", "edad": 21, "calificacion": 92},
    {"nombre": "Miguel", "edad": 23, "calificacion": 75},
    {"nombre": "Luisa", "edad": 20, "calificacion": 50}
]


# Definimos la función que filtra al estudiante con nota igual o superior a 90.
def buena_nota(estudiante):
    return estudiante["calificacion"] >= 90

# Aplica el filtro bueno o malo
estudiantes_destacados = list(filter(buena_nota, estudiantes))

# devuelve a los estudiantes con calificación >= 90
print("Estudiantes con calificación mayor o igual a 90:")
for estudiante in estudiantes_destacados:
    print(f"{estudiante['nombre']} tiene una calificación de: {estudiante['calificacion']}")


# %%
## 19. Crea una función lambda que filtre los números impares de una lista dada.

# mi lista de numeros:
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# en impares, guardo los impares de la lista "numeros"

impares = list(filter(lambda x: x % 2 != 0, numeros))

print(impares)  

# %%
## 20. Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int. Usa la función filter()

# mi lista de elementos: 

lista_elementos = [1, 'Python', 10, 'me resulta', 20, 'horrible']

# me filtra solo los enteros:

solo_enteros = list(filter(lambda x: isinstance(x, int), lista_elementos))

print(solo_enteros)  

# %%
## 21. Crea una función que calcule el cubo de un número dado mediante una función lambda

# la funcion lambda la asigno a la variable cubo 
cubo = lambda x: x ** 3

# %%
numero = 2
resultado = cubo(numero)

# %%
print(f"El cubo de {numero} es: {resultado}")

# %%
## 22. Dada una lista numérica, obtén el producto total de los valores de dicha lista. Usa la función reduce()
 
from functools import reduce    # necesito traerme la funcion

# Lista numérica:
lista_numerica = [1, 2, 3, 4]

# Función que multiplica dos números x e y
def multiplicar(x, y):
    return x * y

# ahora, el valor del producto total lo almaceno aqui:
producto_total = reduce(multiplicar, lista_numerica)

print(f"El producto total es: {producto_total}")

# %%
## 23. Concatena una lista de palabras. Usa la función reduce()

from functools import reduce    ## para traerme la función reduce

# Lista de palabras
lista_palabras = ["Python", " no", " me", " gusta"]

# Función que concatena dos strings
def concatenar(x, y):
    return x + y

# ahora, la lista de palabras concatenada la almaceno aqui usando reduce:
frase = reduce(concatenar, lista_palabras)

print(f"La frase es: {frase}")


# %%
## 24. Calcula la diferencia total en los valores de una lista. Usa la función reduce()

from functools import reduce   ## me traigo la funcion reduce()

# mi lista de valores y defino la funcion restar
valores = [50, 5, 5]

def restar(x, y):
    return x - y

diferencia_total = reduce(restar, valores)

print(f"La diferencia total es: {diferencia_total}")



# %%
## 25. Crea una función que cuente el número de caracteres en una cadena de texto dada.

## utilizo la funcion len() que cuenta el numero de caracteres en una cadena string

cadena_texto = "Hoy ha salido el sol"
numero_de_caracteres = len(cadena_texto)

print(f"La cadena de texto cuenta con {len(cadena_texto)} caracteres")

# %%
## 26. Crea una función lambda que calcule el resto de la división entre dos números dados.

# creo la variable resto donde almacenará el resto de la division x entre y
resto = lambda x, y: x % y

print(resto(10, 6)) 

# %%
print(f"El resto de la división es: {resto(10,6)}")

# %%
## 27. Crea una función que calcule el promedio de una lista de números

# defino la lista de numeros
lista_numeros = [100, 24, 12, 42, 0]

promedio = sum(lista_numeros) / len(lista_numeros)

print(f"El promedio es {promedio}")

# %%
## 28. Crea una función que busque y devuelva el primer elemento duplicado en una lista dada

def primer_duplicado(lista):

    # creo el conjunto donde se irán almacenando los elementos
    conjunto = set()  
    for elemento in lista:
        if elemento in conjunto:
            return elemento  # devuelve el primer duplicado encontrado
        conjunto.add(elemento)  # va añadiendo los numeros uno a uno
    return None  # para que me devuelva None en el caso de que no haya ningun duplicado en la lista

# %%
lista = [3, 1, 6, 2, 3, 5, 1, 8]
resultado = primer_duplicado(lista)

if resultado:
    print(f"El primer elemento duplicado de la lista es: {resultado}")
else:
    print("No hay elementos duplicados")

# %%
## 29. Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el carácter '#', 
# excepto los últimos cuatro.


# defino la funion enmascarar:
def enmascarar(variable):
    # Convertimos la variable a cadena de texto, creando la variable "texto"
    texto = str(variable)

    # Si la longitud es menor o igual a 4, no enmascaramos nada
    if len(texto) <= 4:
        return texto

    # Reemplazamos todos los caracteres menos los últimos 4 con '#'
    enmascarado = "#" * (len(texto) - 4) + texto[-4:]

    return enmascarado


print(enmascarar(123456789))       
print(enmascarar("Hola"))  
print(enmascarar(1234))            
print(enmascarar("Python"))          

# %%
## 30.	Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras pero en diferente orden.

def son_anagramas(palabra1, palabra2):
    return sorted(palabra1) == sorted(palabra2)

# %%
palabra1="amor"
palabra2="roma"

if son_anagramas(palabra1, palabra2):
    print(f"Las palabras '{palabra1}' y '{palabra2}' son anagramas")
else:
    print(f"Las palabras '{palabra1}' y '{palabra2}' no son anagramas")

# %%
print(son_anagramas("amor", "roma")) 

# %%
## 31. Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en
## esa lista. Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se
## lanza una excepción

def buscar_nombre():
    try:
        print("Ingresa una lista de nombres:")
        entrada = input()    ## aqui se supone que ingreso la lista de nombres
        lista_nombres = []   ## aqui se van almacenando los nombres
        for nombre in entrada.split(','):
            lista_nombres.append(nombre.strip())
        print("Ingresa el nombre que quieres buscar:")
        nombre_a_buscar = input().strip()   ## strip quita los posibles espacios que hay en la lista de nombres
        if nombre_a_buscar in lista_nombres:
            print(f"¡El nombre '{nombre_a_buscar}' se encuentra en la lista!")
        else:
            raise ValueError(f"El nombre '{nombre_a_buscar}' no se encuentra en la lista")
    except ValueError as e:
        print("Error:", e)

# %%
buscar_nombre()

# %%
## 32. Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y
## devuelve el puesto del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona
## no trabaja aquí.

def buscar_puesto_interactivo():
    # Lista de empleados (nombre, puesto)
    empleados = [
        ("Ana Gómez", "Administradora"),
        ("Luis Pérez", "Contador"),
        ("Marta Díaz", "Recepcionista"),
        ("Miguel Sánchez", "Programador"),
    ]

    # Mostrar el mensaje antes del input 
    print("Ingresa el nombre completo del empleado que deseas buscar:")
    nombre_completo = input().strip()

    # Buscar el nombre en la lista
    for nombre, puesto in empleados:
        if nombre_completo == nombre:
            print(f"El puesto de {nombre_completo} es: {puesto}")
            return  # Terminamos la función si se encuentra

    # Si llegamos aquí, no se encontró
    print(f"{nombre_completo} no trabaja aquí.")

# %%
buscar_puesto_interactivo()

# %%
## 33. Crea una función lambda que sume elementos correspondientes de dos listas dadas.

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

resultado = list(map(lambda x, y: x + y, lista1, lista2))
print(resultado)



# %%
## 34. Crea la clase Arbol , define un árbol genérico con un tronco y ramas como atributos. Los métodos disponibles son:
## crecer_tronco, nueva_rama, crecer_ramas, quitar_rama e info_arbol. El objetivo es implementar estos métodos para manipular la estructura del árbol.

## PASO 1: Crear la clase Arbol
class Arbol:
    def __init__(self):
        self.tronco = 1  # Longitud inicial del tronco
        self.ramas = []  # Lista vacía de ramas

## PASO 2: Método crecer_tronco

## Este método aumenta el tronco en 1 unidad.

    def crecer_tronco(self):
        self.tronco += 1

## PASO 3: Método nueva_rama

## Este método agrega una nueva rama con longitud 1.

    def nueva_rama(self):
        self.ramas.append(1)

## PASO 4: Método crecer_ramas

## Este método aumenta en 1 unidad la longitud de todas las ramas existentes.

    def crecer_ramas(self):
        self.ramas = [rama + 1 for rama in self.ramas]

## PASO 5: Método quitar_rama

## Este método elimina una rama en una posición específica (índice de la lista).
## Vamos a hacerlo con control de errores por si el índice no existe.

    def quitar_rama(self, posicion):
        if 0 <= posicion < len(self.ramas):
            del self.ramas[posicion]
        else:
            print("No existe una rama en esa posición.")

## PASO 6: Método info_arbol

## Este método muestra la información del árbol:

## Longitud del tronco

## Número de ramas

## Longitud de cada rama

    def info_arbol(self):
        print("Longitud del tronco:", self.tronco)
        print("Número de ramas:", len(self.ramas))
        print("Longitudes de las ramas:", self.ramas)

## Caso de uso:
## 1. Crear un árbol.
mi_arbol = Arbol()
## 2. Hacer crecer el tronco del árbol una unidad.
mi_arbol.crecer_tronco()
## 3. Añadir una nueva rama al árbol.
mi_arbol.nueva_rama()
## 4. Hacer crecer todas las ramas del árbol una unidad.
mi_arbol.crecer_ramas()
## 5. Añadir dos nuevas ramas al árbol.
mi_arbol.nueva_rama()
mi_arbol.nueva_rama()
## 6. Retirar la rama situada en la posición 2.
mi_arbol.quitar_rama(2)
## 7. Obtener información sobre el árbol.
mi_arbol.info_arbol()









# %%
## 36. Crea la clase UsuarioBanco, representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta corriente.
# Proporciona métodos para realizar operaciones como retirar dinero, transferir dinero desde otro usuario y agregar dinero al saldo. 

## PASO 1: Crear la clase UsuarioBanco

# Necesitamos guardar en esta clase:

# El nombre del usuario
# El saldo de la cuenta
# Si tiene cuenta corriente o no (True o False)

class UsuarioBanco:
    def __init__(self, nombre, saldo, cuenta_corriente):
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente

## PASO 2: Método retirar_dinero

## Este método va a restar el dinero del saldo. Si el saldo es menor a lo que se retira, dará un error

    def retirar_dinero(self, cantidad):
        if cantidad > self.saldo:
            raise ValueError(f"{self.nombre} no tiene suficiente saldo para retirar {cantidad} unidades.")
        self.saldo -= cantidad

## PASO 3: Método transferir_dinero

## Este método recibe otro objeto UsuarioBanco porque la transferencia tiene que ser de otro usuario, y una cantidad x.
## Saca dinero del otro usuario y lo agrega al usuario actual

## Importante, saber que el otro usuario tiene suficiente saldo para la transferencia.

    def transferir_dinero(self, otro_usuario, cantidad):
        if cantidad > otro_usuario.saldo:
            raise ValueError(f"{otro_usuario.nombre} no tiene suficiente saldo para transferir {cantidad} unidades.")
        otro_usuario.saldo -= cantidad
        self.saldo += cantidad

## PASO 4: Método agregar_dinero

## Suma dinero al saldo del usuario actual

    def agregar_dinero(self, cantidad):
        self.saldo += cantidad

## PAso 5: Método info_usuario

## Para ver el estado del usuario fácilmente (nombre, saldo, cuenta corriente):

    def info_usuario(self):
        print(f"Nombre: {self.nombre}")
        print(f"Saldo: {self.saldo}")
        print(f"Cuenta corriente: {self.cuenta_corriente}")

## CAso de uso
# 1. Crear dos usuarios
alicia = UsuarioBanco("Alicia", 100, True)
bob = UsuarioBanco("Bob", 50, True)

# 2. Agregar 20 unidades de saldo a Bob
bob.agregar_dinero(20)

# 3. Transferir 80 unidades desde Bob a Alicia
alicia.transferir_dinero(bob, 80)

# 4. Retirar 50 unidades del saldo de Alicia
alicia.retirar_dinero(50)

# Mostrar la info de ambos
print("\nEstado final de las cuentas:")
alicia.info_usuario()
print()
bob.info_usuario()

# %%
## 37.	Crea una función llamada procesar_texto que procesa un texto según la opción especificada:
# contar_palabras, reemplazar_palabras, eliminar_palabra.
# Estas opciones son otras funciones que tenemos que definir primero y llamar dentro de la función procesar_texto.

# %%
# 1. Función para contar palabras
def contar_palabras(texto):
    palabras = texto.split()  # Divide el texto en palabras
    contador = {}
    for palabra in palabras:
        if palabra in contador:
            contador[palabra] += 1
        else:
            contador[palabra] = 1
    return contador

# 2. Función para reemplazar palabras
def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    return texto.replace(palabra_original, palabra_nueva)

# 3. Función para eliminar una palabra
def eliminar_palabra(texto, palabra_a_eliminar):
    palabras = texto.split()
    resultado = []
    for palabra in palabras:
        if palabra != palabra_a_eliminar:
            resultado.append(palabra)
    return ' '.join(resultado)

# 4. Función principal que usa las otras funciones según la opción
def procesar_texto(texto, opcion, *args):
    if opcion == "contar":
        return contar_palabras(texto)
    elif opcion == "reemplazar":
        return reemplazar_palabras(texto, args[0], args[1])
    elif opcion == "eliminar":
        return eliminar_palabra(texto, args[0])
    else:
        return "Opción no válida"
    

texto = "Estoy estudiando Python y Python no me gusta"

# Contar palabras
print("Contar:", procesar_texto(texto, "contar"))

# Reemplazar palabra 'Python' por 'SQL'
print("Reemplazar:", procesar_texto(texto, "reemplazar", "Python", "SQL"))

# Eliminar palabra 'no'
print("Eliminar:", procesar_texto(texto, "eliminar", "no"))

# %%
## 38. Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario.

# defino la hora que será introducida en el terminal
hora = int(input("Introduce la hora (siempre numeros enteros de 0 a 23): "))

if  7 <= hora <= 13:
    print("Es de día")
elif 14 <= hora <= 19:
    print("Es por la tarde")
elif 0 <= hora <= 6 or 20 <= hora <= 23:
    print("Es de noche")
else:
    print("Hora no válida")

# %%
## 39. Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica.
## Las reglas de calificación son:
## - 0 - 69 insuficiente
## - 70 - 79 bien
## - 80 - 89 muy bien
## - 90 - 100 excelente

# defino la calificacion introduciendo en el terminal:
calificacion = int(input("Introduce tu calificación (0 a 100): "))

if 0 <= calificacion <= 69:
    print("Insuficiente")
elif 70 <= calificacion <= 79:
    print("Bien")
elif 80 <= calificacion <= 89:
    print("Muy bien")
elif 90 <= calificacion <= 100:
    print("Excelente")
else:
    print("Calificación no válida")

# %%
print(calificacion)

# %%
## 40. Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo" , "circulo" o
## "triangulo" ) y datos (una tupla con los datos necesarios para calcular el área de la figura).

# importo este módulo:  para poder usar el numero pi
import math  

# para el rectangulo:
def calcular_area(figura, datos):
    if figura == "rectangulo":
        base, altura = datos
        return base * altura

    elif figura == "triangulo":
        base, altura = datos
        return (base * altura) / 2
    
    elif figura == "circulo":
        radio, = datos  # La coma es necesaria para desempaquetar una tupla de un solo valor
        return math.pi * (radio ** 2)
    else:
        return "Figura no válida"

# %%
## 41. En este ejercicio, se te pedirá que escribas un programa en Python que utilice condicionales para determinar el
## monto final de una compra en una tienda en línea, después de aplicar un descuento. El programa debe hacer lo siguiente:
## 1. Solicita al usuario que ingrese el precio original de un artículo.
## 2. Pregunta al usuario si tiene un cupón de descuento (respuesta sí o no).
## 3. Si el usuario responde que sí, solicita que ingrese el valor del cupón de descuento.
## 4. Aplica el descuento al precio original del artículo, siempre y cuando el valor del cupón sea válido (es decir, mayor
## a cero). Por ejemplo, descuento de 15€.
## 5. Muestra el precio final de la compra, teniendo en cuenta el descuento aplicado o sin él.
## 6. Recuerda utilizar estructuras de control de flujo como if, elif y else para llevar a cabo estas acciones en tu
## programa de Python.

def calcular_precio_final():
    # 1. Solicita al usuario que ingrese el precio original del artículo
    try:
        precio_original = float(input("Ingresa el precio original del artículo: "))
    except ValueError:
        print("Por favor, ingresa un número válido para el precio")
        return  
    
# 2. Preguntamos si tiene cupón de descuento (salvo las diferentes formas de escribir)
    tiene_cupon = input("¿Tienes un cupón de descuento? (sí/no): ").strip().lower()

    # Inicializamos descuento a 0
    descuento = 0

# 3. Si responde sí, pedimos el valor del cupón:
    if tiene_cupon == "sí" or tiene_cupon == "si":
        try:
            valor_cupon = float(input("Ingresa el valor del cupón de descuento en euros: "))
        except ValueError:
            print("El valor del cupón debe ser un número válido.")
            return

# 4. Aplicamos descuento solo si es mayor que cero
        if valor_cupon > 0:
            descuento = valor_cupon
        else:
            print("El valor del cupón debe ser válido. No se aplicará descuento.")
    elif tiene_cupon == "no":
        print("No se aplicará descuento.")


# 5. Calculamos el precio final
    precio_final = precio_original - descuento

    # Para evitar que el precio final sea negativo (si el valor del cupón es mayor que el precio original)
    if precio_final < 0:
       precio_final = 0

    # 6. Mostramos el precio final
    print(f"El precio final de la compra es: {precio_final} €")

# Ejecutamos la función
calcular_precio_final()

# %%
# solicitar que ingrese el precio original
precio_original = float(input("Ingresa el precio original del artículo: "))
print("El precio original es:", precio_original)

# %%
try:
    numero = int(input("Ingresa un número entero: "))
    print("El número es:", numero)
except ValueError:
    print("Eso no es un número entero válido.")


