def double(sequence):
    result = []
    for element in sequence:
        result = result + [element * 2]
    return result

def doubler(sequence):
    if len(sequence) == 0:
        return []
    else:
        return [2 * sequence[0]] + doubler(sequence[1:])

prime = [2, 3, 5, 7, 11]
zero = []
print(doubler(prime))
print(doubler(zero))
