def to_f(c):
    return ((9/5) * c) + 32

# def to_f(c):
#     return ((9.0/5) * c) + 32
#
# def to_f(c):
#     return ((9.0/5.0) * c) + 32

def to_c(f):
    return (5/9) * (f-32)

# def to_c(f):
#     return (5/9.0) * (f-32)

print(to_f(25))
print(to_c(92))

print(to_f(to_c(25)))
print(to_c(to_f(90)))
