# 4.Programming Fundermentals exercise and free project

# Exercise
ex = [-50, 0, 10, 11, 12, 14]

def positive(sequence):
    result = []
    for element in sequence:
        if element > 0:
            result = result + [element]
    print(len(result))
positive(ex)

def pluses(sequence):
    sum = 0
    for element in sequence:
        if element > 0:
           sum = sum + element
    print(sum)
pluses(ex)

# Free project
def minus_div5(sequence_5):
    result_5 = []
    for element_5 in sequence_5:
        result_5 = result_5 + [element_5 / 5]
    return pluses(result_5)

ex_5 = [-80, -21, 0, 1, 55]
minus_div5(ex_5)
