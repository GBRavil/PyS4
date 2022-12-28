# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
num = int(input("Введите число N: "))
first_num = 2
lst = []
old = num
while first_num <= num:
    if num % first_num == 0:
        lst.append(first_num)
        num //= first_num
    else:
        first_num += 1
print(f"Простые множители числа {old} приведены в списке: {lst}")