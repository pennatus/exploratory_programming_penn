def sign(num):
    answer = '?'
    if num > 0:
        answer = '+'
    if num < 0:
        answer = '-'
    if num == 0:
        answer = ''
    return answer

print(sign(4))
print(sign(-20))
print(sign(0))
print(sign(1))

def sign_ver2(num):
    answer = '?'
    if num > 0:
        answer = '+'
    elif num < 0:
        answer = '-'
    else:
        answer = ''
    return answer

# negative index
name = 'Paula'
print(name[-1])
word = 'hello'
print(word[-1])
'world'[-1]
print('world'[-1])

def gender(name):
    if name[-1] == 'a':
        return 'female'
    if name[-1] == 'o':
        return 'male'

print(gender('Apollo'))
print(gender('Nick')) # None

def gender_ver2(name):
    indicated = '?'
    if name[-1] == 'a':
        indicated = 'female'
    if name[-1] == 'o':
        indicated = 'male'
    return indicated
print(gender_ver2('Nick'))
