def caesar(str, u_shift):
    output_string = [(string_al[(string_al.index(sym) + u_shift) % 33]) if sym != ' ' else ' ' for sym in text]
    new_str = ''

    for j in output_string:
        new_str += j
    return new_str


text = input('Введите сообщение: ')
shift = int(input('Введите сдвиг: '))
string_al = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

output = caesar(text, shift)

print('Зашифрованное сообщение:', output)
