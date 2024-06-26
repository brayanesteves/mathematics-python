# [ESP] Este cuaderno tiene como fin, resolver ejercicios de 'Calculo I' (Lo cual es 'Cálculo Diferencial' y 'Cálculo Integral') con ayuda de la librería de 'SymPy'.
# [ENG] This notebook aims to solve exercises of 'Calculus I' (which is 'Differential Calculus' and 'Integral Calculus') with the help of the 'SymPy' library.

import sympy as smp

# [ESP] Integrales Indefinidas.
# [ENG] Indefinite Integrals.

x, y = smp.symbols('x y')

smp.sin(x)**6
smp.integrate(smp.sin(x)**6, x)

1 / (x**4 + 1)
smp.integrate(1 / (x**4 + 1), x)