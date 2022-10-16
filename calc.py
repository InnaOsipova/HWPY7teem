def calculation(a, operation, b):
    result = None
    if operation == '+':
        result = a + b
    elif operation == '-':
        result = a - b
    elif operation == '/':
        result = a / b
    elif operation == '*':
        result = a * b
    else:
        print('Неизвестный оператор')
    return result


def calc_ration():
    user_expression = input('Введите выражение для вычисления в формате: "A знак B"'
                            '\nМежду числами и знаком ставьте пробелы:'
                            '\n').split()
    number_a, number_b = int(user_expression[0]), int(user_expression[2])
    calc_result = calculation(number_a, user_expression[1], number_b)
    result = str("".join(map(str, user_expression)) + " = " + str(calc_result))
    print(result)
    return result


def calc_complex():
    user_expression = input('Введите выражение для вычисления в формате: "A знак B действие C знак D, где:'
                            '\n A и C - действительные части чисел"'
                            '\n B и D - мнимые части чисел'
                            '\n действие - математическая операция которую нужно произвести с двумя числами'
                            '\nМежду числами и знаком ставьте пробелы:'
                            '\n').split()
    a_imaginary_part, b_imaginary_part = user_expression[2], user_expression[6]

    if user_expression[1] == '-':
        a_imaginary_part = float(user_expression[2]) * -1
    if user_expression[5] == '-':
        b_imaginary_part = float(user_expression[6]) * -1

    number_a = complex(float(user_expression[0]), a_imaginary_part)
    number_b = complex(float(user_expression[4]), b_imaginary_part)
    calc_result = calculation(number_a, user_expression[3], number_b)
    result = str("".join(map(str, user_expression)) + " = " + str(calc_result))
    print(result)
    return result
