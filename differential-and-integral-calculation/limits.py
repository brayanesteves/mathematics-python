# [ESP] Este cuaderno tiene como fin, resolver ejercicios de 'Calculo I' (Lo cual es 'Cálculo Diferencial' y 'Cálculo Integral') con ayuda de la librería de 'SymPy'.
# [ENG] This notebook aims to solve exercises of 'Calculus I' (which is 'Differential Calculus' and 'Integral Calculus') with the help of the 'SymPy' library.

import sympy as smp

# [ESP] Limites. Empezamos con limites.
# [ENG] Limits. We start with limits.

x, y = smp.symbols('x y')

(x**2 + 3 * x - 10)/(x**2 + x - 6)
smp.limit((x**2 + 3 * x - 10)/(x**2 + x - 6), x, 2)

smp.tan(1/smp.sin(x) + smp.cos(x))
smp.limit(smp.tan(1/smp.sin(x) + smp.cos(x)), x, smp.ex(1))
smp.limit(smp.tan(1/smp.sin(x) + smp.cos(x)), x, smp.ex(1)).n()

1/(x**2 - 1)
smp.limit(1/(x**2 - 1), x, 1, dir='+')
smp.limit(1/(x**2 - 1), x, 1, dir='-')

(smp.cos(x) - 1) / x
smp.limit((smp.cos(x) - 1) / x, x, smp.oo)