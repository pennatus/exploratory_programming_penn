# 3 Double, Double
def double(sequence):
    result = []
    for element in sequence:
        result = result + [element * 2]
    return result

double([1, 2, 10])
print (double([1, 2, 10]))

double([-42, 0, 42])
print(double([-42, 0, 42]))

double([24])
print(double([24]))

double([])
print(double([]))

x = [1, 2, 3]
double(x)
print (double(x))
