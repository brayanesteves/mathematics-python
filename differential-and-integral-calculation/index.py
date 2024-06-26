# [ESP] Este cuaderno tiene como fin, resolver ejercicios de 'Calculo I' (Lo cual es 'Cálculo Diferencial' y 'Cálculo Integral') con ayuda de la librería de 'SymPy'.
# [ENG] This notebook aims to solve exercises of 'Calculus I' (which is 'Differential Calculus' and 'Integral Calculus') with the help of the 'SymPy' library.

import sympy as smp

x, y = smp.symbols('x y')

# [ESP] Declarando funciones.
# [ENG] Declaring functions.
f_0 = x**3 + 2*y

f_1 = x**(1/3)

f_2 = x**(smp.Rational(1,3))

f_3 = x**(smp.Rational(1,3))
f_3.subs(x,2)

f_4 = x**(smp.Rational(1,3))
f_4.subs(x,2).n()