import math
import ast
import requests


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


def available_time(schedule, slot):
    available = []

    for i in range(0, len(schedule) + 1):
        if i == 0:
            if slot[0] != schedule[i][0]:
                available.append([slot[0], schedule[i][0]])
        elif i == len(schedule):
            if schedule[i - 1][1] != slot[1]:
                available.append([schedule[i - 1][1], slot[1]])
        else:
            available.append([schedule[i - 1][1], schedule[i][0]])
    return available


def clean_available_time(time, limiter):
    result = []
    for i in range(0, len(time)):

        if limiter[0] < time[i][0] < limiter[1] or limiter[0] < time[
                i][1] < limiter[1]:
            if i == 0 and time[i][0] < limiter[0]:
                result.append([limiter[0], time[i][1]])

            elif i == len(time) - 1 and time[i][1] > limiter[1]:
                result.append([time[i][0], limiter[1]])

            else:
                result.append([time[i][0], time[i][1]])

    return result


def intersections(array1, array2):  #[[1,2],[3,4],[5,6]]
    result = []
    for index1 in range(0, len(array1)):
        for index2 in range(0, len(array2)):
            if array1[index1][0] <= array2[index2][0] <= array1[index1][1]:
                if array2[index2][1] < array1[index1][1]:
                    result.append([array2[index2][0], array2[index2][1]])
                else:
                    result.append([array2[index2][0], array1[index1][1]])
            elif array1[index1][0] <= array2[index2][1] <= array1[index1][1]:
                if array2[index2][0] > array1[index1][0]:
                    result.append([array2[index2][0], array2[index2][1]])
                else:
                    result.append([array1[index1][0], array2[index2][1]])
    return result


def available_hours(schedule1, slot1, schedule2, slot2):
    schedule1 = [[cleantime(item) for item in time] for time in schedule1]
    slot1 = [cleantime(item) for item in slot1]
    schedule2 = [[cleantime(item) for item in time] for time in schedule2]
    slot2 = [cleantime(item) for item in slot2]
    limiter = [max(slot1[0], slot2[0]), min(slot1[1], slot2[1])]
    available1 = available_time(schedule1, slot1)
    available2 = available_time(schedule2, slot2)
    available1 = clean_available_time(available1, limiter)
    available2 = clean_available_time(available2, limiter)

    result = intersections(available1, available2)
    result2 = []
    for index in range(0, len(result)):
        result2.append(
            [timed(result[index][0]),
             timed(result[index][1])])
    return result2


print("1er PROGRAMA")
print("ALGORITMO PARA CALCULAR FRANJA HORARIA DISPONIBLE")
print("EN UN DIA PARA DOS TRABAJADORES OCUPADOS")
print(" ")
print("Este es un ejercicio propuesto por la gente")
print("de Google en sus entrevistas laborales.")
print("En teoria demoraria en resolverse (una aproximacion en pseudocodigo) ")
print("en media hora. Personalmente lo pude resolver en 2 horas y algo.")
print("Solo le falta validar la entrada de datos.")
print("github: https://github.com/martinteppa/calendarioPython")
print(" ")
schedule1 = ast.literal_eval(
    input(
        "ingrese el horario de trabajo de la persona 1 en forma de lista, ejemplo: [['9:00', '13:30'], ['14:30', '15:30']]  "
    ))

slot1 = ast.literal_eval(
    input(
        "ingrese la franja horaria laboral de la persona 1 en forma de lista, ejemplo: ['8:00', '17:30']   "
    ))

schedule2 = ast.literal_eval(
    input(
        "ingrese el horario de trabajo de la persona 2 en forma de lista, ejemplo: [['10:00', '13:30'], ['16:00', '16:30']]  "
    ))
slot2 = ast.literal_eval(
    input(
        "ingrese la franja horaria laboral de la persona 2 en forma de lista, ejemplo: ['10:00', '18:40']   "
    ))
print("los horarios disponible para visitas entre ambos son: " +
      str(available_hours(schedule1, slot1, schedule2, slot2)))

print("2do PROGRAMA \n")
print("Vamos a requestear en la api-rest pokeapi")
print(" ")
while True:
    try:
        pokemon_id = int(input("Ingrese el Id de un pokemon del 1 al 898 \n"))
        request = 'https://pokeapi.co/api/v2/pokemon/' + str(pokemon_id)
        r = requests.get(request)

        if r.status_code == 200:
            print("Usted a buscado a: " + r.json()["name"])
        else:
            print(
                "No es posible obtener la request, quizas no exista el pokemon"
            )
    except ValueError:
        print("No ha ingresado un numero entero")

    keep_searching = input(
        "Desea buscar otro pokemon? presione cualquier letra, sino enter\n")
    if not bool(keep_searching):
        break
