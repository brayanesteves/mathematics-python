# [ESP] Este cuaderno tiene como fin, resolver ejercicios de 'Calculo I' (Lo cual es 'Cálculo Diferencial' y 'Cálculo Integral') con ayuda de la librería de 'SymPy'.
# [ENG] This notebook aims to solve exercises of 'Calculus I' (which is 'Differential Calculus' and 'Integral Calculus') with the help of the 'SymPy' library.

import sympy as smp

# [ESP] Integrales Impropias.
# [ENG] Improper Integrals.

x, y = smp.symbols('x y')

1 / (x**2 + 1)
smp.integrate(1 / (x**2 + 1), (x, 0, smp.oo))