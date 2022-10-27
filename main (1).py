while True:
    password = input('Введите пароль: ')
    num = []

    up = [i_lst for i_lst in password]
    pas = [(num.append(i), up.remove(i)) for i in password if i in '1234567890']

    new_up = up[:]

    lst = [new_up.remove(i_word) for i_word in up if i_word != i_word.upper()]

    if len(new_up) >= 1 and len(num) >= 3 and len(password) >= 8:
        print('Пароль надежный!')
        break
    else:
        print('Пароль ненадёжный. Попробуйте ещё раз.')



