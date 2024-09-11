### Idetificador de numero romanos en una cadena de Texto ###
### por Juan S Moreno Posada


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


# Esta funcion valida si hay numeros romanosc
def is_roman(input):
    for letra in input:
        if letra in dict_romanos:
            print('si hay romanos')
            return True

def separate_roman(input):
    array = []
    bandera = False
    for letra in input:
        if letra in dict_romanos:
            bandera = True
            array.append(letra)
        elif bandera:
            break
    return array

def numerar_romanos(input):
    valores = []
    for letra in input:
        if letra in dict_romanos:
            valores.append(dict_romanos[letra])
    return valores

def evaluar_valores(array):
    array.append(0)
    result = []
    for i in range(len(array)-1):
        if array[i] < array[i+1]:
            result.append(array[i] *(-1))
        else:
            result.append(array[i])
    print(sum(result))

def is_valid(array):
    result = []
    bandera = 0
    for i in range(len(array)-1):
        if input[i] == 'V' or input[i] == 'L' or input[i] == 'D':
            if input[i] == input[i+1]:
                print(f'No pueden ir dos {input[i]} seguidas')
        if input[i] == 'I' or input[i] == 'X' or input[i] == 'C' or input[i] == 'M':
            if input[i] == input[i+1]:
                bandera +=1
    if bandera > 2:
            print("no puede haber mas de 3 letras iguales")    

def sintax_checker(input):
    for i in range(len(input)-1):
        if input[i] == 'I' or input[i] == 'L' :
            if input[i+1] != 'I' and input[i+1] != 'V' and input[i+1] != 'X':
                print(f'error de sintaxis despues de {input[i]} solo puede ir I, V o X ') 
        if input[i] == 'V':
            if input[i+1] != 'I':
                print(f'error de sintaxis despues de {input[i]} solo puede ir I')
        if input[i] == 'X':
            if input[i+1] == 'M':
                print(f'error de sintaxis despues de {input[i]} solo puede ir I,V,X,L o C ')  
            
##m main
input = 'Xiilena'
input = input.upper()


is_roman(input)
is_valid(input)


romanos = separate_roman(input)

print(romanos)
sintax_checker(romanos)
roman_value = numerar_romanos(romanos)
print(roman_value)
evaluar_valores(roman_value)

