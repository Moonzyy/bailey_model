import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

#  Импортируем модуль для работы с анимацией:
import matplotlib.animation as animation

n = 200
a = 100
t = np.linspace(0, 1.5, 300)
def f(t, x, b, c): return -b * x * (n + a - x)

fig = plt.figure(figsize=(10,5))
ax = plt.axes()
plt.legend(['x', 'y'], shadow=True)

def animate(b):
    ax.clear()
    ax.set(title=f"Динамика численности незараженных x(t), зараженных y(t) особей без учета выздоровления при \nb={round(b, 3)}",
      xlabel='x',
      ylabel='x,y')
    ax.legend("s")
    ax.grid()
    sol = solve_ivp(f, [0, 3], [n], args=(b, 0), dense_output=True)
    z = sol.sol(t)
    line1 = ax.plot(t, z.T, 'b')
    line2 = ax.plot(t, a + n - z.T, 'r')
    return line1, line2

f_animation = animation.FuncAnimation(fig, 
                                      animate, 
                                      frames=np.linspace(0, 0.05, 100),
                                      interval = 500,
                                      repeat = False)

#save gif
/*f_animation.save('not_recovery.gif',
                 writer='imagemagick', 
                 fps=30)*/
