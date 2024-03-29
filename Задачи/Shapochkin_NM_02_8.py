import re


"""
В России применяются регистрационные знаки нескольких видов. Общего в них то, что они состоят из цифр и букв. 
Причём используются только 12 букв кириллицы, имеющие графические аналоги в латинском алфавите — А, В, Е, К, М, Н, О, Р, С, Т, У и Х.
У частных легковых автомобилях номера — это буква, три цифры, две буквы, затем две или три цифры с кодом региона. 
У такси — две буквы, три цифры, затем две или три цифры с кодом региона. Есть также и другие виды, но в этой задаче они не понадобятся.

Вам потребуется определить, является ли последовательность букв корректным номером указанных двух типов, и если является, то каким.

На вход даются строки, которые претендуют на то, чтобы быть номером. Определите тип номера. 
Буквы в номерах — заглавные русские. Маленькие и английские для простоты можно игнорировать.
"""
def identify_car_number(numbers):
    car_temp = r'\b[АВЕКМНОРСТУХ]{1}\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}\b'
    taxi_temp = r'\b[АВЕКМНОРСТУХ]{2}\d{3}\d{2,3}\b'

    for line in numbers:
        if re.fullmatch(car_temp, line):
            print(f'{line}: car')
        elif re.fullmatch(taxi_temp, line):
            print(f'{line}: taxi')
        else:
            print(f'{line}: invalid input')

# identify_car_number(['123D213kd', 'А123ВА29', 'ЕЕ23429'])

"""
Слово — это последовательность из букв (русских или английских), внутри которой могут быть дефисы. 
На вход даётся текст, посчитайте, сколько в нём слов. PS. Задача решается в одну строчку. 
Никакие хитрые техники, не упомянутые выше, не требуются. Прочитать текст из файла.
"""

# text = input('Введите текст: ')
# print(len(re.findall(r'\s', text))+1)

"""
Вовочка подготовил одно очень важное письмо, но везде указал неправильное время. 
Поэтому нужно заменить все вхождения времени на строку (TBD). 
Время — это строка вида HH:MM:SS или HH:MM, в которой HH — число от 00 до 23, а MM и SS — число от 00 до 59. 
(ВВОД: Уважаемые! Если вы к 09:00 не вернёте чемодан, то уже в 09:00:01 я за себя не отвечаю. 
ВЫВОД: Уважаемые! Если вы к (TBD) не вернёте чемодан, то уже в (TBD) я за себя не отвечаю. )
"""
def replace_time():
    text = input('Введите текст: ')

    time = r'\b([0-1]\d|2[0-3])(:[0-5]\d)\b'
    big_time = time + r'\b([0-1]\d|2[0-3])(:[0-5]\d){2}\b'
    text = re.sub(time, '[TBD]', text)
    text = re.sub(big_time, '[TBD]', text)
    print(text)

# replace_time()
    
"""
Владимир устроился на работу в одно очень важное место. И в первом же документе он ничего не понял, 
там были сплошные ФГУП НИЦ ГИДГЕО, ФГОУ ЧШУ АПК и т.п. Тогда он решил собрать все аббревиатуры, 
чтобы потом найти их расшифровки на http://sokr.ru/. Помогите ему. Будем считать аббревиатурой слова 
только лишь из заглавных букв (как минимум из двух). Если несколько таких слов разделены пробелами, 
то они считаются одной аббревиатурой.
"""

def find_abbreviation():
    text = input('Введите текст: ')
    template = r'[А-Я]{2,}(?: [А-Я]{2,}){0,}'
    print(re.findall(template, text))

find_abbreviation()