dict_romanos = {
    'I' : 1,
    'V' : 5,
    'X' : 10,
    'L' : 50,
    'C' : 100,
    'D' : 500,
    'M' : 1000
}

input = 'xlivn'
input = input.upper()

def is_roman(input):
    for letra in input:
        if letra in dict_romanos:
            print('si hay romanos')
            return True

def separate_roman(input):
    array = []
    for letra in input:
        if letra in dict_romanos:
            array.append(letra)
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

##m main

is_roman(input)
array_romanos = separate_roman(input)
print(array_romanos)
valores = numerar_romanos(array_romanos)
print(valores)
evaluar_valores(valores)