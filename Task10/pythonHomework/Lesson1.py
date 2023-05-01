# Задача 2: Найдите сумму цифр трехзначного числа.

number = int(input("Enter a three-digit number: "))
d1 = number // 100
d2 = number % 100 // 10
d3 = number % 10
print(f"{d1} + {d2} + {d3} = {d1 + d2 + d3}")


# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, 
# что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

total = int(input("Enter the total amount of items made: "))
petya = int(total / 6)
sereja = int(total / 6)
katya = int((total / 6) * 4)
if total % 2 == 0:
    print(f"Items made per person:\n\tPetya: {petya}\n\tKatya: {katya}\n\tSereja: {sereja}")
else:
    print("Нельзя определить")


# Задача 6: Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех. 
# Вам требуется написать программу, которая проверяет счастливость билета.

ticket = str(input("Enter 6-digit ticket number: "))
sumLeft = int(ticket[0]) + int(ticket[1]) + int(ticket[2])
sumRight = int(ticket[-3]) + int(ticket[-2]) + int(ticket[-1])
print(f"{sumLeft} : {sumRight}")
if sumLeft == sumRight:
    print("Congratulations! It's a lucky ticket.")
else:
    print("It's NOT a lucky ticket. Better luck next time!")


# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками 
# (то есть разломить шоколадку на два прямоугольника).
# 3 2 4 -> yes
# 3 2 1 -> no

n = int(input("Введите длину шоколадки: "))
m = int(input("Введите ширину шоколадки: "))
k = int(input("Введите количество долек: "))
if k < n * m and ((k % n == 0) or (k % m == 0)):
    print("Да")
else:
    print("Нет")