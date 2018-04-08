len('hello world')
len('2112')
len('')

hi = 'hello world'
print(len(hi))

hi2 = "hello world"
print(len(hi2))

# print(len(2112)) TypeError: object of type 'int' has no len()

print('hello'[0])
print('hello'[1])
print('hello'[2])
print('hello'[3])
print('hello'[4])

# print('hello'[5]) IndexError: string index out of range

print('hello world'[0:3])
# print(''[0]) IndexError: string index out of range
print(''[0:1])
print('hello world'[0:500])
print('hello world'[450:500])

print('hello world'[:3])
print('hello world'[1:])

print('abcdefgh'[0:9:2])
print('abcdefgh'[::2])
print('0123456789'[::2])

print('hello world'[-1:])

wyatt = 'They flee from me that sometime did me seek / With naked foot, stalking in my chamber.'

print('HELLO World'.lower())
original = 'Burma Shave'
lowercase = original.lower()
print(lowercase)
wyatt = wyatt.lower()
print(wyatt)

for c in wyatt:
    print(c)

for i in range(len(wyatt)):
    print(wyatt[i])

for i in range(len(wyatt)):
    print(i, wyatt[i])

for i in range(len(wyatt)):
    print(wyatt[i:i+2])

# pair = 0
# for i in range(len(wyatt)):
#     if wyatt[i:i+2] == 'ee':
#         pair = pair + 1
# print(pair)

# pair = 0
# for i in range(len(wyatt)):
#     if wyatt[i] == wyatt[i+1]: IndexError: string index out of range
#         pair = pair + 1
# print(pair)

pair = 0
for i in range(len(wyatt)-1):
    if wyatt[i] == wyatt[i+1]:
        pair = pair + 1
