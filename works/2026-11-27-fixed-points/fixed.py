"""Полевой определитель неподвижных точек: три экземпляра, живьём.  python3 fixed.py"""
import math

# 1. Банах: сжимающее отображение. cos сжимает на [0,1], итерируй откуда угодно.
def banach(f, x, eps=1e-12):
    n = 0
    while abs(f(x) - x) > eps:
        x, n = f(x), n + 1
    return x, n

x, n = banach(math.cos, 0.0)
print(f"Банах:  cos(x)=x  ->  {x:.10f}  за {n} шагов")

# 2. Клини: наименьшая неподвижная точка функционала. Факториал как предел
#    приближений: F(f)(n) = 1 if n==0 else n*f(n-1); старт — «нигде не определена».
F = lambda f: (lambda n: 1 if n == 0 else n * f(n - 1))
approx = lambda n: (_ for _ in ()).throw(RecursionError("⊥"))
for k in range(6):
    approx = F(approx)          # после k шагов знаем факториал для n < k
def show(f, n):
    try: return f(n)
    except RecursionError: return "⊥"
print("Клини:  F^6(⊥) на 0..8 ->", [show(approx, n) for n in range(9)])

# 3. Квайн: программа — неподвижная точка отображения «запустить».
import subprocess, sys, pathlib
src = pathlib.Path(__file__).with_name("quine.py")
out = subprocess.run([sys.executable, str(src)], capture_output=True, text=True).stdout
print("Квайн:  вывод совпадает с исходником ->", out == src.read_text())
