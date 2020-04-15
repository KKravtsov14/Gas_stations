import io
def dictionary_file():
    with io.open('azs.txt', encoding='utf-8') as f:
        lst, lst_auto, lst_car, lst_oil = [], [], [], []
        for _ in f:
            a = _.replace('\n', '')
            automat = 'Автомат_' + str(a[0])
            countcar = a[2]
            oil = a[4:].split()
            lst_auto.append(automat)
            lst_car.append(countcar)
            lst_oil.append(oil)
            lst.append(a)
    slovar_info = {}
    for k in range(len(lst)):
        slovar = [lst_auto[k], {'Очередь': int(lst_car[k]), 'Бензин': lst_oil[k]}]
        slovar_info[slovar[0]] = slovar[1]
    print(slovar_info)


dictionary_file()