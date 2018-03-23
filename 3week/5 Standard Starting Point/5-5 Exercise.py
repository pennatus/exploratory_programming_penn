# Exercise 1. Negative Factorial fix
def fact(n):
    if n == 0:
        return 1
    if n < 0:
        return ''
    else:
        return n * fact(n-1)
print(fact(-5))
print(fact(10))

# Exercise 2. Factorial Mash-Up
def fact_ver2(n):
    if n >= 0:
        answer = 1
        for num in range(1, n+1):
            answer *= num
        return answer
    else:
        return ''

print(fact_ver2(-5))
