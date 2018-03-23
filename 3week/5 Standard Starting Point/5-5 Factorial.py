# 버전별로 range 함수가 차이가 있는듯...?
print(range(5))
print(range(1,6))
print(list(range(5)))
print(list(range(1,6)))

def factorial(n):
    answer = 1
    for num in range(1, n+1):
        answer *= num
    return answer
print(factorial(5))
print(factorial(0))

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)
print(fact(5))
