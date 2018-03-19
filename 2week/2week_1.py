# 4.Programming Fundermentals
# 4.1 Abstracting Related Code: Functions
print(4 + 4.5 + 0.375)
print(1500 * 0.08875)
print(995.50 * 0.08875)

def tax(subtotal):
    return subtotal * 0.08875

print(tax(1500))

print(1500 + tax(1500))
print(200 + 1500 + tax(1500))

sum = 1500
sum = sum + (sum * 0.08875) # Add the tax amount

def set_a():
    a = 10
    print('the value of a:', a)

set_a()
a = 20
print('Initially, the value of a:', a)
set_a()
print('Finally, the value of a:', a)

def scoped(first, second):
    third = second + second - first
    return third
first = 10
second = 12
print(scoped(2, 4))

# 4.2 Abstracting along Sequences: Iteration
l = [7, 4, 2, 6]
for num in l:
    print(num)

for num in l:
    print(num * 2)

def mean(sequence):
    total = 0.0
    for element in sequence:
        total = total + element
    return total/len(sequence)

# def mean_1(sequence):
#     total = 0
#     for element in sequence:
#         total = total + element
#     return total/len(sequence)

print(mean([1,2]))
# print(mean_1([1,2]))

short = [5, 5, 5, 5]
print(mean(short))
short_1 = [-5, 0, 5]
print(mean(short_1))

# 4.3 Abstracting across Types: Polymorphism
x = 5
print(type(x))
print(type(5))

x = 'Hello world'
print(type(x))

x = [1, 2, 3]
print(type(x))
print(type([1, 2, 3]))

print(type('hello'+'world'))
print(type('knock'+'knock'))

a = 'hello'
b = 'world'
print(a + b)

print(len('Hello world'))
print(len([1, 2, 3]))
# print(len(5))
# print(len(2 + 'hello'))

print(len(str(5)))
print((str(2)+'hello'))

# 4.4 Revisiting double()
volume = [4.0, 2.0, 3.0, 5.5]
result = []
for element in volume:
    result = result + [element * 2]
print(result)

def double(sequence):
    result = []
    for element in sequence:
        result = result + [element * 2]
    return result

words = ['hello', 'world']
print(double(words))

countdown = [3, 2, 1, 'contact']
print(double(countdown))

print(double('abstraction'))

# 4.5 Another Fundermentals: The conditional
def secret(word):
    if word == 'please':
        return 'Yes!'

print(secret('hello'))
print(secret('world'))
print(secret('please'))
print(secret(' please'))

def yesno(word):
    if word == 'yes':
        return True
    if word == 'no':
        return False
print(yesno('haha'))
print(yesno('no'))
print(yesno('yes'))
print(yesno('Yes'))

def secret_1(word):
    if word == 'please':
        return 'Yes!'
    else:
        return 'No.'
print(secret_1('hello'))
print(secret_1('world'))
print(secret_1('please'))
print(secret_1(' please'))

def secret_2(word):
    if word == 'please':
        return True
    else:
        return False
print(secret_2('hello'))
print(secret_2('world'))
print(secret_2('please'))
print(secret_2(' please'))

def secret_3(word):
    return (word == 'please')
print(secret_3('hello'))
print(secret_3('world'))
print(secret_3('please'))
print(secret_3(' please'))

# 4.6  Division and Types
# "The core work ... will be done in Python, specifically Python 2.7"
print(7 / 2)
print(7.0 / 2)
print(7.0 / 2.0)
print(7 / 2.0)
print(7 * 0.5)
print((0.0 + 1 + 2) / 2)
print((0 + 1 + 2) / 2)
print('hi' * 2)
# print('hihi' / 2)
