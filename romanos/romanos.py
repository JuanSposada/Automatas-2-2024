### Idetificador de numero romanos en una cadena de Texto ###
### por Juan S Moreno Posada

## Este programa extrae los numeros romanos de una cadena de texto
## lo tiene, verifica que su sintaxis para que sea valida de acuerdo
##c con las reglas de los numeros romanos
## Despues nos devuelve el valor del numero romano valido

# Diccionario de valores romanos
dict_romanos = {
    'I' : 1,
    'V' : 5,
    'X' : 10,
    'L' : 50,
    'C' : 100,
    'D' : 500,
    'M' : 1000
}

array_palabras = ['pixel', 'civil', 'paco', 'hijo', 'toxico','camion', 'clave', 'ximena', 'damian',
                  'lili', 'claudia', 'medallon', 'clima']

# Esta funcion valida si hay numeros romanos
def is_roman(entrada):
    for letra in entrada:
        if letra in dict_romanos:
            print('si hay romanos')
            return True


"""Esta funcion separa los numeros romanos de la cadena de texto
    y los coloca en un arreglo"""
def separate_roman(entrada):
    array = []
    #bandera = False
    for letra in entrada:
        if letra in dict_romanos:
            bandera = True
            array.append(letra)
     #   elif bandera:
     #       break
    return array

"""Esta funcion saca los valores de los numeros romanos de acuerdo al diccionario"""
def numerar_romanos(entrada):
    valores = []
    for letra in entrada:
        if letra in dict_romanos:
            valores.append(dict_romanos[letra])
    return valores

""" Esta funcion hace la suma de los numeros romanos 
    si el valor esta  la izquierda de uno mayor, se multiplica por -1
    para que al final se sume y este automaticamente se reste del resultado"""
def evaluar_valores(array):
    array.append(0)
    result = []
    for i in range(len(array)-1):
        if array[i] < array[i+1]:
            result.append(array[i] *(-1))
        else:
            result.append(array[i])
    return(sum(result))

""" Verifica si hay caracteres dupliccados mas de 3 veces"""
def is_duplicate(entrada):
    entrada.append(0)
    result = []
    bandera = 0
    for i in range(len(entrada)-1):
        result.append(entrada[i])
        if entrada[i] == entrada[i+1]:
            bandera +=1
        if bandera > 2:
            print("no puede haber mas de 3 letras iguales")
            break
    return result

""" Verifica la sintaxis de acuerdo a las reglas de los numeros romanos
    hasta que queda un arreglo con el numero completo  y valido romano"""
def sintax_checker(entrada):
    result = []
    entrada.insert(0,0)
    entrada.append(0)
    for i in range(len(entrada)-1):
        if entrada[i] == 'I':
            result.append(entrada[i])
            if entrada[i+1] != 'I' and entrada[i+1] != 'V' and entrada[i+1] != 'X':
                print(f'error de sintaxis despues de {entrada[i]} solo puede ir I, V o X ') 
                break
        if entrada[i] == 'V':
            result.append(entrada[i])
            if entrada[i+1] != 'I':
                print(f'error de sintaxis despues de {entrada[i]} solo puede ir I')
                break
            if entrada[i-1] == "I" and entrada[i+1]:
                print("Error, despues de IV no puede ir I ")
                break
        if entrada[i] == 'X':
            result.append(entrada[i])
            if entrada[i+1] == 'M':
                print(f'error de sintaxis despues de {entrada[i]} solo puede ir I,V,X,L o C ')
                break
            if entrada[i-1] == 'I' and entrada[i+1]:
                print('error, despues de IX no puede ir otra I')  
                break
        if entrada[i] == 'L':
            result.append(entrada[i])
            if entrada[i+1] != 'I' and entrada[i+1] != 'V' and entrada[i+1] != 'X':
                print(f'error de sintaxis despues de {entrada[i]} solo puede ir I, V o X ')
                break
            if entrada[i-1] == 'X' and entrada[i+1]=='X':
                print('Error,  despues de XL, no puede haber otra X')
                break
        if entrada[i] == 'D':
            result.append(entrada[i])
            if entrada[i+1] == 'M':
                print(f'error de sintaxis despues de D solo puede ir I, V,  X, L, C ')
                break
            if entrada[i-1] == 'C' and entrada[i+1] == 'C':
                print("Error de sintaxis, despues de CD no puede haber otra C")
                break
        if entrada[i] == 'C' or entrada[i] == 'M':
            result.append(entrada[i])
    return result

##m main

def main():
    dict_palabras = {}
    for entrada in array_palabras:

        entrada = entrada.upper()

        if is_roman(entrada):

            romanos = separate_roman(entrada)
            print(romanos)
            checked_romanos= sintax_checker(romanos)
            print(checked_romanos)
            checked_duplicates = is_duplicate(checked_romanos)
            roman_value = numerar_romanos(checked_duplicates)
            print(roman_value)
            resultado = evaluar_valores(roman_value)
            dict_palabras[entrada] = resultado
            print(dict_palabras)
    ordered_palabras = {k: v for k, v in sorted(dict_palabras.items(), key=lambda item: item[1])}
    print("\nPalabras ordenadas: \n")
    print(ordered_palabras)

main()