# Сначала вводится число N, затем вводится ровно N целых чисел. Подсчитайте, сколько из них равны нулю, и выведите это количество.

n = int(input("Введите количество чисел "))
a = 0 # добавление счетчика

#if (n > 0):
   # for i in range(0, n+1):
    #s = int(input("Введите целое число: "))

for i in range(n):
    s = int(input("введите целое число "))

    if s == 0:
        a += 1

print(a)