# Exercise 1. A Conversion Experience
def in_cm(i):
    return i * (254/100)
def cm_in(m):
    return m / (254/100)

print(cm_in(30))
print(in_cm(30))

# Exercise 2. Categorical, Imperative
def length(word):
    if len(word) >= 10:
        return 'Long.'
    else:
        return 'Short.'

print(length('world'))
print(length('pollopescovegetarianism'))
