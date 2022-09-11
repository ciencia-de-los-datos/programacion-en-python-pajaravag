"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""



def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    data = open("data.csv", "r").readlines()
    data = [line.replace('\n', '') for line in data]
    data = [line.replace('\t', ',') for line in data]
    data = [line.split(',') for line in data]

    result = 0.0
    col_2 = [pos[1] for pos in data]
    for i in col_2:
        result += int(i) 
    return result


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    data = open('data.csv', 'r').readlines()
    data = [line.replace('\n', '') for line in data]
    data = [line.replace('\t', ',') for line in data]
    data = [line.split(',') for line in data]
    times = []
    col_1 = [pos[0] for pos in data]
    result = []
    for i in list(set(col_1)):
        times.append(col_1.count(i))
    result = sorted(list(zip(list(set(col_1)),times)))

    return result


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    data = open('data.csv', 'r').readlines()
    data = [line.replace('\n', '') for line in data]
    data = [line.replace('\t', ',') for line in data]
    data = [line.split(',') for line in data]
    sumas = []
    for x in list(set([pos[0] for pos in data])):
        X = [row for row in data if row[0] == x]
        X = [int(row[1]) for row in X]
        sumas.append(sum(X))
    result = sorted(list(zip(list(set([pos[0] for pos in data])), sumas)))
    return result


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    data = open('data.csv', 'r').readlines()
    data = [line.replace('\n', '') for line in data]
    data = [line.replace('\t', ',') for line in data]
    data = [line.split(',') for line in data]
    X = [pos[2] for pos in data]
    X = [mes[5:7] for mes in X]
    result = []
    times =[]
    for i in list(set(X)):
        times.append(X.count(i))
    result = sorted(list(zip(list(set(X)),times)))
    return result


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    data = open('data.csv', 'r').readlines()
    data = [line.replace('\n', '') for line in data]
    data = [line.replace('\t', ',') for line in data]
    data = [line.split(',') for line in data]
    col_1 = [pos[0] for pos in data]
    col_2 = [pos[1] for pos in data]
    value_min = []
    value_max = []
    for x in list(set(col_1)):
        X = [row for row in data if row[0] == x]
        X = [int(row[1]) for row in X]
        value_min.append(min(X))
        value_max.append(max(X))

    result = sorted(list(zip(list(set(col_1)), value_max, value_min)))
    return result


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    col5 = open("data.csv", "r").readlines()
    col5 = [line.replace('\n', '') for line in col5]
    col5 = [line.split('\t')[4] for line in col5]
    col5 = [line.split(',') for line in col5]
    tripletas = set([element.split(':')[0] for row in col5 for element in row])
    flat_list = [item for sublist in col5 for item in sublist]
    value_min, value_max, temp_list = [], [], []
    for value in tripletas:
        X = [int(element.split(':')[1]) for element in flat_list if element.split(':')[0] == value]
        value_min.append(min(X))
        value_max.append(max(X))
    result = sorted(list(zip(tripletas, value_max, value_min)))
    return result


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    data = open('data.csv', 'r').readlines()
    data = [line.replace('\n', '') for line in data]
    data = [line.replace('\t', ',') for line in data]
    data = [line.split(',') for line in data]
    col_1 = [pos[0] for pos in data]
    col_2 = [pos[1] for pos in data]
    col_2 = [int(element) for element in col_2]
    temp_list = []
    for number in set(col_2):
        X = [col_1[pos] for pos in range(len(col_1)) if number == col_2[pos]]
        temp_list.append(X)
    result = sorted(list(zip(set(col_2), temp_list)))
    return result


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    return


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    return


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    return


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    return


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    return
