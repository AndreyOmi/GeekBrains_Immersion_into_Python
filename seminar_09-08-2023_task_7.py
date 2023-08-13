""" Задача № 7:
Пользователь вводит число от 1 до 999. 
Используя операции с числами сообщите что введено: цифра, двузначное число или трёхзначное число.
Для цифры верните её квадрат, например 5 - 25
Для двузначного числа произведение цифр, например 30 - 0
Для трёхзначного числа его зеркальное отображение, например 520 - 25
Если число не из диапазона, запросите новое число
Откажитесь от магических чисел
В коде должны быть один input и один print """

while True:
    number = int(input("Введите число от 1 до 999: "))

    if number < 1 or number > 999:
        print("Число введено за пределами диапазона. Введите новое число.")
        continue
    elif number < 10:
        square = number ** 2
        print(f"Число из одной цифры. Квадрат числа {number} - {square}")
        break
    elif number < 100:
        digit_product = (number // 10) * (number % 10)
        print(f"Число двухзначное. Произведение цифр числа {number} - {digit_product}")
        break
    else:
        reversed_number = int(str(number)[::-1])
        print(f"Число трехзначное. Зеркальное отображение числа {number} - {reversed_number}")
        break