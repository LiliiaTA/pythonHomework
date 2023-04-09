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


