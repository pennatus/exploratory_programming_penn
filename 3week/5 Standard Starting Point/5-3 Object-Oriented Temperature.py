class Temperature(object):
    def __init__(self, value):
        self._celsius = float(value)
    def c(self):
        return str(self._celsius) + ' C'
    def f(self):
        return str((self._celsius * (9.0/5.0)) + 32.0) + ' F'

boil = Temperature(100)
boil.c()
# line9에서 syntax error가 계속 났었는데... line7의 괄호 갯수 실수를 수정하니 사라짐...

freeze = Temperature(0)
freeze.f()

fine = Temperature(23)

print(boil.c())
print(boil.f())
print(freeze.c())
print(freeze.f())
#
# print(boil + fine) >> TypeError: unsupported operand type(s) for +: 'Temperature' and 'Temperature'

class Tmp(object):
    def __init__(self, value):
         self._celsius = float(value)
    def c2(self):
        return str(self._celsius) + ' C'
    def f2(self):
        return str((self._celsius * (9.0/5.0)) + 32.0) + ' F'
    def __init__(self, value, scale):
        if scale.lower() == 'c':
            self._celsius = float(value)
        elif scale.lower() == 'f':
            self._celsius = (value - 32) * (5.0/9.0)
        else:
            raise Exception("Unknown Scale; use 'c' or 'f'.")

cool = Tmp(56, 'f')
cool.c2()
print(cool.c2())

# oops = Tmp(500, 'a')
# oops.c2()
# print(oops.c2())
# Traceback (most recent call last):
#   File "C:\Users\Ahra\Documents\exploratory_programming\penn\3week\5 Standard Starting Point\5-3 Object-Oriented Temperature.py", line 44, in <module>
#     oops = Tmp(500, 'a')
#   File "C:\Users\Ahra\Documents\exploratory_programming\penn\3week\5 Standard Starting Point\5-3 Object-Oriented Temperature.py", line 38, in __init__
#     raise Exception("Unknown Scale; use 'c' or 'f'.")
# Exception: Unknown Scale; use 'c' or 'f'.
