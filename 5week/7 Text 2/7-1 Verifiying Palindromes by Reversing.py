list('rotor')
to_test = list('rotor')
print(to_test)

test = ['a','b','c']
test.reverse()
print(test)
# ''.join(test))

# word = 'hierarchy'
# backlist = list(word)
# backlist.reverse()
# print(backlist)

def pal(word):
    backlist = list(word)
    backlist.reverse()
    return backlist == list(word)
print(pal('rotor'))

def pal_2(word):
    lo_word = word.lower()
    backlist = list(lo_word)
    backlist.reverse()
    return backlist == list(lo_word)
print(pal_2('RoTor'))

alpha = 'abcdefghijklmnopqrstuvwxyz'
alphaback = alpha[::-1]
print(alphaback)
