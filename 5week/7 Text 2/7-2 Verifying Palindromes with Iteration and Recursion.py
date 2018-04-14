original = 'Civic'
string = original.lower()
print((string[0] == string[-1]))

right = -1
pal = True
for letter in string:
    pal = (pal and (letter == string[right]))
    right = right - 1

right = -1
pal = True
for letter in string:
    pal = (pal and (letter == string[right]))
    print(letter + string[right] + ': ' + str(letter == string[right]))
    right = right -1

# def pali(string):
#     right = -1
#     pal = True
#     for letter in string:
#         pal = (pal and (letter == string[right]))
#         if letter == string[right]:
#             right = right - 1
#         else:
#             return False
#     return True
# print(pali('cadhaskdaksrhqkhakfc'))

def pal(text):
    return text.lower() == text[::-1].lower()
print(pal('civfaaic'))

def palr(text):
    lowercase = text.lower()
        if len(lowercase) <= 1:
            return True
        else:
            if lowercase[0] == lowercase[-1]:
                return palr(lowercase[1:-1])
            else:
                return False
