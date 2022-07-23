'''
Пробелы в выражениях и инструкциях
Избегайте использования пробелов в следующих ситуациях:
'''


# Непосредственно внутри круглых, квадратных или фигурных скобок.
# Правильно:
spam(ham[1], {eggs: 2})

# Неправильно:
spam( ham[ 1 ], { eggs: 2 } )


# Непосредственно перед запятой, точкой с запятой или двоеточием:
# Правильно:
if x == 4: print(x, y); x, y = y, x

# Неправильно:
if x == 4 : print(x , y) ; x , y = y , x


# Сразу перед открывающей скобкой, после которой начинается список аргументов при вызове функции:
# Правильно:
spam(1)

# Неправильно:
spam (1)


# Сразу перед открывающей скобкой, после которой следует индекс или срез:
# Правильно:
dict['key'] = list[index]

# Неправильно:
dict ['key'] = list [index]


# Использование более одного пробела вокруг оператора присваивания (или любого другого) для того, чтобы выровнять его с другим:
# Правильно:
x = 1
y = 2
long_variable = 3

# Неправильно:
x             = 1
y             = 2
long_variable = 3

'''
Другие рекомендации
Всегда окружайте эти бинарные операторы одним пробелом с каждой стороны: 
присваивания (=, +=, -= и другие), 
сравнения (==, <, >, !=, <>, <=, >=, in, not in, is, is not), 
логические (and, or, not).
Если используются операторы с разными приоритетами, 
попробуйте добавить пробелы вокруг операторов с самым низким приоритетом. 
Используйте свои собственные суждения, однако, 
никогда не используйте более одного пробела, 
и всегда используйте одинаковое количество пробелов 
по обе стороны бинарного оператора.
'''


# Правильно:
i = i + 1
submitted += 1
x = x*2 - 1
hypot2 = x*x + y*y
c = (a+b) * (a-b)

# Неправильно:
i=i+1
submitted +=1
x = x * 2 - 1
hypot2 = x * x + y * y
c = (a + b) * (a - b)


# Не используйте пробелы вокруг знака =, 
# если он используется для обозначения именованного аргумента 
# или значения параметров по умолчанию.
# Правильно:
def complex(real, imag=0.0):
    return magic(r=real, i=imag)

# Неправильно:
def complex(real, imag = 0.0):
    return magic(r = real, i = imag)
Не используйте составные инструкции (несколько команд в одной строке).

# Правильно:
if foo == 'blah':
    do_blah_thing()
do_one()
do_two()
do_three()

# Неправильно:
if foo == 'blah': do_blah_thing()
do_one(); do_two(); do_three()


'''
Иногда можно писать тело циклов while, 
for или ветку if в той же строке, 
если команда короткая, 
но если команд несколько, 
никогда так не пишите. 
А также избегайте длинных строк!
'''


# Точно неправильно:
if foo == 'blah': do_blah_thing()
for x in lst: total += x
while t < 10: t = delay()

# Вероятно, неправильно:
if foo == 'blah': do_blah_thing()
else: do_non_blah_thing()

try: something()
finally: cleanup()

do_one(); do_two(); do_three(long, argument,
                             list, like, this)

if foo == 'blah': one(); two(); three()

# Данный скрипт запускать не надо!