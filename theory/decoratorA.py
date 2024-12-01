from functools import wraps

def decorator(func):
    @wraps(func)
    def inner(*args, **kwargs):
        print('функция начинается...')
        func(*args, **kwargs)
        print('функция заканчивается')
    return inner

def say(name, surname, age):
    print('Hello', name, surname, age)

d = decorator(say) # вместо d, say, получается декоратор
d('вав', 'ЬАЬ', 12)

say = decorator(say)
say('Vasya', 'Pusechkin', 21)




def header(func):

    def inner(*args, **kwargs):
        print('<VA>')
        func(*args, **kwargs)
        print('</VA>')
    return inner

def table(func):

    def inner(*args, **kwargs):
        print('<h>')
        func(*args, **kwargs)
        print('</h>')
    return inner

def vav(name, surname, age):
    print('Hello', name, surname, age)

vav = table(header(vav))
vav('1', '2', '3')

# декоратор навешивают
@header
@table # hello = header(table(hello))
def hello(name, surname, age):
    print('Hello!!', name, surname, age)

hello('Vasiliy', 'Vasilev', 23)