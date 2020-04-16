import random as rnd
import math as m


def dictionary_file():
    with open('azs.txt', 'r') as f:
        number_stations = 0
        lst, lst_auto, lst_car, lst_oil = [], [], [], []
        for _ in f:
            number_stations += 1
            a = _.replace('\n', '')
            automat = 'Автомат №' + str(a[0])
            countcar = a[2]
            oil = a[4:].split()
            lst_auto.append(automat)
            lst_car.append(countcar)
            lst_oil.append(oil)
            lst.append(a)
    slovar_info = {}
    for k in range(len(lst)):
        slovar = [lst_auto[k], {'Максимальная очередь:': int(lst_car[k]), 'Марки бензина:': lst_oil[k]}]
        slovar_info[slovar[0]] = slovar[1]
    return slovar_info, number_stations


def reader():
    with open('input.txt', 'r') as f:

        slovar_info, number_stations = dictionary_file()
        slovar_clients = {}
        for i in list(slovar_info.keys()):
            slovar_clients[i] = []

        for i in f:

            time, volume, gas = map(str, i.split())
            volume = int(volume)
            for j in range(number_stations):

                key_j = 'Автомат №' + str(j + 1)
                if len(slovar_clients[key_j]) != 0:
#вывести на экран выезжающих, если их время раньше нового времени
                    if int(time.replace(':', '')) >= int(slovar_clients[key_j][0][0].replace(':', '')): # Надо бы красивше сделать

                        print('В', slovar_clients[key_j][0][0], 'клиент', slovar_clients[key_j][0][1],
                              slovar_clients[key_j][0][2], slovar_clients[key_j][0][3], slovar_clients[key_j][0][4],
                              'заправил свой автомобиль и покинул АЗС.')
#удалить список с отъезжающим автомобилем
                        slovar_clients[key_j] = slovar_clients[key_j][1:]

                    for g in range(number_stations):
#вывести информацию про оставшиеся автомобили
                        key_g = 'Автомат №' + str(g + 1)
                        lst_keys = list(slovar_info[key_g].keys())
                        number_autos = '*' * len(slovar_clients[key_g])

                        print(key_g, lst_keys[0], slovar_info[key_g][lst_keys[0]], lst_keys[1],
                              slovar_info[key_g][lst_keys[1]], '->', number_autos)


#проверить автоматы с подходящим бензином
            number_stations_w_gas = []
            for j in range(number_stations):

                key_j = 'Автомат №' + str(j + 1)
                lst_keys = list(slovar_info[key_j].keys())
                if gas in slovar_info[key_j][lst_keys[1]]:
                    number_stations_w_gas.append((j + 1, len(slovar_clients[key_j])))

            number_stations_w_gas.sort(key=lambda i: (i[1], i[0]))

#вычислить время заправки
            number_station = 'Автомат №' + str(number_stations_w_gas[0][0])
            len_autos = len(slovar_clients[number_station])

            time_refueling = 0
            while time_refueling == 0:
                time_refueling = m.ceil(volume / 10) + rnd.randint(-1, 1)

            if len_autos == 0:
                time_departure_min = int(time[3:]) + time_refueling
                time_departure_hrs = int(time[:2])

            else:
                time_departure_min = int(slovar_clients[number_station][len_autos - 1][0][3:]) + time_refueling
                time_departure_hrs = int(slovar_clients[number_station][len_autos - 1][0][:2])

            if time_departure_min >= 60:

                if time_departure_hrs < 23:
                    time_departure_hrs += 1
                    time_departure_min = time_departure_min - 60

                else:
                    time_departure_hrs = 0
                    time_departure_min = time_departure_min - 60

            if time_departure_min < 10:
                time_departure_min = '0' + str(time_departure_min)
            else:
                time_departure_min = str(time_departure_min)

            if time_departure_hrs < 10:
                time_departure_hrs = '0' + str(time_departure_hrs)
            else:
                time_departure_hrs = str(time_departure_hrs)

            time_departure = time_departure_hrs + ':' + time_departure_min

            lst_append = [time_departure, time, gas, volume, time_refueling]

#внести все данные в соответствующую очередь или отправить автомобиль и вывести результат на экран
            if len(slovar_clients[number_station]) < slovar_info[number_station]['Максимальная очередь:']:
                slovar_clients['Автомат №' + str(number_stations_w_gas[0][0])].append(lst_append)

                print('В', time, 'новый клиент:', time, gas, volume,
                      time_refueling, 'встал в очередь к автомату №', number_stations_w_gas[0][0])

                for g in range(number_stations):
            # вывести информацию про оставшиеся автомобили
                    key_g = 'Автомат №' + str(g + 1)
                    lst_keys = list(slovar_info[key_g].keys())
                    number_autos = '*' * len(slovar_clients[key_g])

                    print(key_g, lst_keys[0], slovar_info[key_g][lst_keys[0]], lst_keys[1],
                          slovar_info[key_g][lst_keys[1]], '->', number_autos)

            else:
                print('В', time, 'новый клиент:', time_departure, gas, volume,
                      time_refueling, 'не смог заправить автомобиль и покинул АЗС.')

                for g in range(number_stations):
            # вывести информацию про оставшиеся автомобили
                    key_g = 'Автомат №' + str(g + 1)
                    lst_keys = list(slovar_info[key_g].keys())
                    number_autos = '*' * len(slovar_clients[key_g])

                    print(key_g, lst_keys[0], slovar_info[key_g][lst_keys[0]], lst_keys[1],
                          slovar_info[key_g][lst_keys[1]], '->', number_autos)



reader()