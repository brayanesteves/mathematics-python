# [ESP] Este cuaderno tiene como fin, resolver ejercicios de 'Calculo I' (Lo cual es 'Cálculo Diferencial' y 'Cálculo Integral') con ayuda de la librería de 'SymPy'.
# [ENG] This notebook aims to solve exercises of 'Calculus I' (which is 'Differential Calculus' and 'Integral Calculus') with the help of the 'SymPy' library.

import sympy as smp

# [ESP] Integrales Definidas.
# [ENG] Definite Integrals.

x, y = smp.symbols('x y')

(2 - x) * smp.sqrt(x)
smp.integrate((2 - x) * smp.sqrt(x), (x, 0, 2))
smp.integrate((2 - x) * smp.sqrt(x), (x, 0, 2)).n()

x * smp.cos(x**2)
smp.integrate(x * smp.cos(x**2), (x, 0, smp.pi/2))
smp.integrate(x * smp.cos(x**2), (x, 0, smp.pi/2)).n()

t = smp.symbols('t')
x**7 * smp.exp(x)
smp.integrate(x**7 * smp.exp(x), (x, 0, t))