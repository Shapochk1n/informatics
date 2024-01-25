import os

"""
Напишите функцию read_last(lines, file), которая будет открывать определенный файл file 
и выводить на печать построчно последние строки в количестве lines (на всякий случай проверим, 
что задано положительное целое число). Протестируем функцию на файле article.txt со следующим содержимым:
"""
def read_last(lines, file):
    if type(lines) != int:
        print('ERROR')
        return
    if lines == 0:
        return
    opened_file = open(file, 'r', encoding='utf-8')
    all_lines = opened_file.readlines()
    all_lines = [line.rstrip() for line in all_lines]
    for line in all_lines[-lines:]:
        print(line)

read_last(3, 'article.txt')

"""
Выберите любую папку на своем компьютере, имеющую вложенные директории. 
Выведите на печать в терминал ее содержимое, как и всех подкаталогов при помощи функции print_docs(directory).
"""
def print_docs(directory):
    with os.scandir(directory) as listOfEntries:  
        for entry in listOfEntries:
            if entry.is_file():
                print(entry.name)
            elif entry.is_dir():
                print_docs(f'{directory}/{entry.name}')

print_docs('.')

"""
Документ article.txt содержит следующий текст:
Вечерело
Жужжали мухи
Светил фонарик
Кипела вода в чайнике
Венера зажглась на небе
Деревья шумели
Тучи разошлись
Листва зеленела

Требуется реализовать функцию longest_words(file), которая выводит слово, 
имеющее максимальную длину (или список слов, если таковых несколько).
"""

def longest_words(file):
    opened_file = open(file, 'r', encoding='utf-8')
    all_lines = opened_file.readlines()
    all_lines = [line.rstrip() for line in all_lines]
    words = []
    for line in all_lines:
        words += line.split()
    longest_len = len(max(words, key=len))
    res = []
    for word in words:
        if len(word) == longest_len:
            res.append(word)
    print(res)

longest_words('article.txt')


"""
Составьте программу - простейший редактор текстовых файлов. Алгоритм работы программы:

Программа предлагает ввести имя будущего файла. Записывает его, присваивая расширение .txt.
Программа предлагает записать строку в файл. При каждом нажатии кнопки ENTER происходит запись строки и переход на новую строчку.
Если строка пустая или спец. символ - программа сохраняет файл.
"""

def editor():
    file = input('Введите имя файла: ')
    file = open(f'{file}.txt', 'w+')
    while True:
        line = input('Введите строку: ')
        symbols = list('!"$%&()*+,-./:;<=>?@[]^_{|}~')
        if line == '' or (len(line) == 1 and line in symbols):
            break
        file.write(line)
    file.close()

editor()