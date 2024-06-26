# [ESP] Este cuaderno tiene como fin, resolver ejercicios de 'Calculo I' (Lo cual es 'Cálculo Diferencial' y 'Cálculo Integral') con ayuda de la librería de 'SymPy'.
# [ENG] This notebook aims to solve exercises of 'Calculus I' (which is 'Differential Calculus' and 'Integral Calculus') with the help of the 'SymPy' library.

import sympy as smp

# [ESP] Derivadas.
# [ENG] Derivatives.

x, y = smp.symbols('x y')

x**2
smp.diff(x**2, x)

smp.log((smp.sqrt(x**2 + 1) - x)/(smp.sqrt(x**2 - 1) + x))
smp.diff(smp.log((smp.sqrt(x**2 + 1) - x)/(smp.sqrt(x**2 - 1) + x)), x)

smp.tan(4*x**4 - 2*x**2 + (7/2) * x**(-1) + 5)**(-2)
smp.diff(smp.tan(4*x**4 - 2*x**2 + (7/2) * x**(-1) + 5)**(-2), x)

f, g = smp.symbols('f, g', cls=smp.Function)
f = f(x)
g = g(x)
z = f*g

smp.diff(z, x)