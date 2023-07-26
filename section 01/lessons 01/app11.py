# python functions
# a function is a group of statements that performs a particular task

def myfunction():
    x = 'Hello Derkos'
    print(x)

myfunction()


def hello(name):
    x = 'Hello '+name
    print(x)

hello('Angono')


def add_nums(num1, num2):
    x = num1 + num2
    print('Sum is',x)

add_nums(12,34)


def xhello(name='Tirel'):
    x = 'Hello '+name
    return x

print(xhello('Maria'))
print(xhello())


def addit(x,y):
    return x+y

print('Using function:',addit(100,200))

# lambda: arguments, expression
addnow = lambda x,y: x+y
print('Using lambda:',addnow(100,200))









