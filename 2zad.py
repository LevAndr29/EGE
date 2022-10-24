from itertools import permutations as perm
result = {0: 'x', 1: 'y', 2: 'z', 3: 'w'}

def prov(pr):
    for p in perm(range(len(res)), len(res)):  # перебор всех строк в результате
        verno = 0  # проверка совпадений в строках
        for t in range(len(otv)):  # будем проверять только строки в ответах
            stroka = p[t]  # подбор первых строк из нашего перебора
            for ind in range(4):  # проверка всех элементов
                if res[stroka][pr[ind]] not in otv[t][ind]:  # проверка совпадения по элементам
                    break  # если не совпадают выходим из цикла
            else:  # если дошли до конца цикла и не вышли, то
                verno += 1  # увеличиваем совпадение
        if verno == len(otv):  #  если совпадение равно количеству строк в ответе,
            return True  # возвращаем истину

res = []
for x in [0, 1]:
    for y in [0, 1]:
        for z in [0, 1]:
            for w in [0, 1]:
                f = ((not(z == w)) <= (w and (not x)) or (x and (not y)))  #33747
                # f = (x  or (not y)) and (not (w == z)) and w  # 18704
                #f = (z and y) or ((x <= z) == (y <= w)) # 15939
                # f = ((y <= x) and (z or w)) <= ((x and (not w)) or (y == z))# 40977
                if f == 0:
                    res.append([str(x), str(y), str(z), str(w)])
                    # print(x, y, z, w)

otv = [['0', '01', '0', '0'], ['0', '01', '01', '0'], ['0', '01', '01', '01']]  # 33747
# otv = [['1', '01', '0', '0'], ['1', '0', '0', '1'], ['1', '0', '01', '01']]  # 18704
# otv = [['01', '01', '10', '1'], ['1', '01', '01', '1'], ['1', '01', '1', '1']]  # 15939
# otv = [['1', '0', '0', '0'], ['1', '1', '0', '1'], ['01', '01', '01', '0']]  # 40977

for por in perm(range(4), 4):
    if prov(por):  # если вернули истину выводим результат
        for i in range(4):
            print(result[por[i]], end='')
        break