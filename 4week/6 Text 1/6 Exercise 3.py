# Counting Nonspaces
text = 'Alice is my lovely friend.'

def count_nonspaces(arg):
    num = 0
    for a in arg:
        if a != ' ':
            num = num + 1
    return num
print(count_nonspaces(text))

def count_spaces(arg):
    num = 0
    for a in arg:
        if a == ' ':
            num = num + 1
    return num

def count_nonspaces2(arg):
    print(len(arg)-count_spaces(arg))
count_nonspaces2(text)
