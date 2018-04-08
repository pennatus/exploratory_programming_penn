# Counting Spaces
text = 'Alice is my lovely friend.'

def count_spaces(arg):
    num = 0
    for a in arg:
        if a == ' ':
            num = num + 1
    return num
print(count_spaces(text))

def count_spaces2(arg):
    print(len(arg.split(' ')) - 1)
count_spaces2(text)

# def count_spaces3():
