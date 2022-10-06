#  1- Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
#  'абвгдейка - это передача' = >" - это передача"

def delete_abc(Text):
    TextABC = Text.lower().split()
    string_text = " ".join(map(str,[i for i in TextABC if 'абв' not in i]))
    print(string_text);

Text = input(f'Введите текст: ')
delete_abc(Text)