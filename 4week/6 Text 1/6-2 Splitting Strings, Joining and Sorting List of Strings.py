text = 'All human beings are born free and equal in dignity and rights. They are endowed with reason and conscience and should act towards one another in a spirit of brotherhood.'
print(len(text))
print(text.split(' '))
print(text)
print(len(text.split(' ')))
print(text.split('and'))
hi = 'hello   world'
print(hi.split(' '))
print('hello   world'.split(' '))
print(hi.split())

names = ['Bob', 'Carol', 'Ted', 'Alice']
print(' & '.join(names))
# print(names.join(' & ')) AttributeError: 'list' object has no attribute 'join'
print(' and/or '.join(names))
print('\n'.join(names))
print(' exists.\n'.join(names) + ' exists.')

for person in names:
    print(person + ' exists.')

print(sorted(names)) #sorted alphabetically
# print(names.sort())
