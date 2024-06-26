# [ESP] Este cuaderno tiene como fin, resolver ejercicios de 'Calculo I' (Lo cual es 'Cálculo Diferencial' y 'Cálculo Integral') con ayuda de la librería de 'SymPy'.
# [ENG] This notebook aims to solve exercises of 'Calculus I' (which is 'Differential Calculus' and 'Integral Calculus') with the help of the 'SymPy' library.

import sympy as smp

# [ESP] Sumas.
# [ENG] Sum.

n = smp.symbols('n')

1/n**2
smp.Sum(1/n**2, (n, 1, 5))
smp.Sum(1/n**2, (n, 1, 5)).doit()
smp.Sum(1/n**2, (n, 1, 5)).n()

smp.Sum(1/n**2, (n, 1, smp.oo))
smp.Sum(1/n**2, (n, 1, smp.oo)).doit()
smp.Sum(1/n**2, (n, 1, smp.oo)).n()

2 / (n**2 - 1)
smp.Sum(2 / (n**2 - 1), (n, 2, smp.oo))
smp.Sum(2 / (n**2 - 1), (n, 2, smp.oo)).doit()
smp.Sum(2 / (n**2 - 1), (n, 2, smp.oo)).n()