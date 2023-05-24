# Задача 26:  Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8

# def deg(a, b, count=0, res=1):
#     while count < b:
#         res = res * a
#         count += 1
#     return res
#
#
# print(deg(10, 3))

def deg(a, b, count=0, res=1):
    if count < b:
        return deg(a, b, count + 1, res * a)
    return res


print(deg(3, 5))

