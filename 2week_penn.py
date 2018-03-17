# 3 Double, double free project
def div_5(sequence):
    result = []
    for element in sequence:
        result = result + [element / 5]
    return result

div_5([1, 2, 10])
print (div_5([1, 2, 10]))

div_5([-42, 0, 42])
print(div_5([-42, 0, 42]))

div_5([24])
print(div_5([24]))

div_5([])
print(div_5([]))

x = [1, 2, 3]
div_5(x)
print (div_5(x))
