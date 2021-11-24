import sympy
import scipy.integrate
import numpy as np
import matplotlib.pyplot as plt


def F(y_, x_):
    return -2 * y_


x = sympy.Symbol('x')
y = sympy.Function('y')(x)

X = np.linspace(0, 10, 101)
diff = sympy.Eq(y.diff(x) + 2 * y, 0)
eq = sympy.dsolve(diff, ics={y.subs(x, 0): sympy.sqrt(2)})
y_sym = [eq.evalf(subs={x: i}).args[1] for i in X]

y_sci = scipy.integrate.odeint(F, np.sqrt(2), X)

fig, ax = plt.subplots(2, figsize=(8, 10))
ax[0].plot(X, y_sym, label='Sympy')
ax[0].plot(X, y_sci, '--', label='Scipy')
ax[0].grid()
ax[0].legend()

ax[1].plot(X, [abs(y_sym[i] - y_sci[i]) for i in range(len(y_sym))])
ax[1].set_title('Разница между Sympy и Scipy')
ax[1].grid()
plt.show()
