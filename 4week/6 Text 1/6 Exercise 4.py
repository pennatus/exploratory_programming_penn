# Determining Initials
text = 'Georges Perec'

def initials(str):
    for elem in str.split():
        print(elem[0], end='')

initials(text)
