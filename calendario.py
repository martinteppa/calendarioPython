import math
import ast


def cleantime(time):
    (h, m) = time.split(":")
    result = int(h) * 3600 + int(m) * 60
    return result


def timed(time):
    hours = format((math.floor((time / 3600))), '.0f')
    minutes = format(((time % 3600) / 60), '.0f')
    if int(minutes) < 10:
        minutes = "0" + minutes
    if int(hours) < 10:
        hours = "0" + hours
    return hours + ":" + minutes


def tiempodisponible(tiempo1, lapso1):
    tiempodisponible1 = []

    for i in range(0, len(tiempo1) + 1):
        if i == 0:
            if lapso1[0] != tiempo1[i][0]:
                tiempodisponible1.append([lapso1[0], tiempo1[i][0]])
        elif i == len(tiempo1):
            if tiempo1[i - 1][1] != lapso1[1]:
                tiempodisponible1.append([tiempo1[i - 1][1], lapso1[1]])
        else:
            tiempodisponible1.append([tiempo1[i - 1][1], tiempo1[i][0]])
    return tiempodisponible1


def limpiartiempodisponible(tiempo, limitador):
    resultado = []
    for i in range(0, len(tiempo)):

        if limitador[0] < tiempo[i][0] < limitador[1] or limitador[0] < tiempo[
                i][1] < limitador[1]:
            if i == 0 and tiempo[i][0] < limitador[0]:
                resultado.append([limitador[0], tiempo[i][1]])

            elif i == len(tiempo) - 1 and tiempo[i][1] > limitador[1]:
                resultado.append([tiempo[i][0], limitador[1]])

            else:
                resultado.append([tiempo[i][0], tiempo[i][1]])

    return resultado


def intersecciones(array1, array2):  #[[1,2],[3,4],[5,6]]
    resultado = []
    for index1 in range(0, len(array1)):
        for index2 in range(0, len(array2)):
            if array1[index1][0] <= array2[index2][0] <= array1[index1][1]:
                if array2[index2][1] < array1[index1][1]:
                    resultado.append([array2[index2][0], array2[index2][1]])
                else:
                    resultado.append([array2[index2][0], array1[index1][1]])
            elif array1[index1][0] <= array2[index2][1] <= array1[index1][1]:
                if array2[index2][0] > array1[index1][0]:
                    resultado.append([array2[index2][0], array2[index2][1]])
                else:
                    resultado.append([array1[index1][0], array2[index2][1]])
    return resultado


def horasdisponibles(tiempo1, lapso1, tiempo2, lapso2):
    tiempo1 = [[cleantime(item) for item in time] for time in tiempo1]
    lapso1 = [cleantime(item) for item in lapso1]
    tiempo2 = [[cleantime(item) for item in time] for time in tiempo2]
    lapso2 = [cleantime(item) for item in lapso2]
    limitador = [max(lapso1[0], lapso2[0]), min(lapso1[1], lapso2[1])]
    tiempodisponible1 = tiempodisponible(tiempo1, lapso1)
    tiempodisponible2 = tiempodisponible(tiempo2, lapso2)
    tiempodisponible1 = limpiartiempodisponible(tiempodisponible1, limitador)
    tiempodisponible2 = limpiartiempodisponible(tiempodisponible2, limitador)

    resultado = intersecciones(tiempodisponible1, tiempodisponible2)
    resultado2 = []
    for index in range(0, len(resultado)):
        resultado2.append(
            [timed(resultado[index][0]),
             timed(resultado[index][1])])
    return resultado2


print("ALGORITMO PARA CALCULAR FRANJA HORARIA DISPONIBLE")
print("EN UN DIA PARA DOS TRABAJADORES OCUPADOS")
print(" ")
print("Este es un ejercicio propuesto por la gente")
print("de Google en sus entrevistas laborales.")
print("En teoria demoraria en resolverse en media hora")
print("Personalmente lo pude resolver en 2 horas y algo.")
print("Solo le falta validar la entrada de datos.")

horario1 = ast.literal_eval(
    input(
        "ingrese el horario de trabajo de la persona 1 en forma de lista, ejemplo: [['9:00', '13:30'], ['14:30', '15:30']]  "
    ))

franja1 = ast.literal_eval(
    input(
        "ingrese la franja horaria laboral de la persona 1 en forma de lista, ejemplo: ['8:00', '17:30']   "
    ))

horario2 = ast.literal_eval(
    input(
        "ingrese el horario de trabajo de la persona 2 en forma de lista, ejemplo: [['10:00', '13:30'], ['16:00', '16:30']]  "
    ))
franja2 = ast.literal_eval(
    input(
        "ingrese la franja horaria laboral de la persona 2 en forma de lista, ejemplo: ['10:00', '18:40']   "
    ))

print("los horarios disponible para visitas entre ambos son: " +
      str(horasdisponibles(horario1, franja1, horario2, franja2)))
