number1 = float(input('Введите первое число: '))
sign = input('Введите знак действия: ')
number2 = float(input('Введите второе число: '))
if sign == '+':
    result = number1 + number2
elif sign == '-':
    result = number1 - number2
elif sign == '*':
    result = number1 * number2
elif sign == '/':
    result = number1 / number2
print("Ответ: ", result)