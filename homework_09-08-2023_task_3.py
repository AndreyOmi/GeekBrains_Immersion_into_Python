""" Задача № 3:
Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
должна подсказывать «больше» или «меньше» после каждой попытки. """

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000


num = randint(LOWER_LIMIT, UPPER_LIMIT)

count_attempts = 0
number_attempts = 10

print('Предлагается угадать целое число между ' + str(LOWER_LIMIT) + ' и ' + str(UPPER_LIMIT))

while count_attempts < number_attempts:
    count_attempts += 1
    print('Попытка ' + str(count_attempts) + ' из ' + str (number_attempts))
    user_num = float(input('Введи целое число между ' + str(LOWER_LIMIT) + ' и ' + str(UPPER_LIMIT) + ': '))
    if user_num == num:
        print('Вы угадали число. Поздравляю.')
        break
    elif user_num < num and user_num >= LOWER_LIMIT:
        print('Введите большее число.')
    elif user_num > num and user_num <= UPPER_LIMIT:
        print('Введите меньшее число.')
    else:
        print('Вы ввели число за заданными пределами. Попробуйте ввести другое число.')
else:
    print('Исчерпаны все попытки. До свидания.')
    
print('Было загадано число ' + str(num))

