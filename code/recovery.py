import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

#  Импортируем модуль для работы с анимацией:
import matplotlib.animation as animation

n = 200
a = 100
g = 0.5
t = np.linspace(0, 10, 300)
def f(t, y, b, g):
    x, u, z = y
    return [-b * x * u, b * x * u - g * u, g * u]

fig = plt.figure(figsize=(10,5))
ax = plt.axes()
plt.legend(['x', 'y'], shadow=True)

def animate(b):
    ax.clear()
    ax.set(title=f"Динамика численности незараженных x(t), зараженных y(t) особей с выздоровлением при \nb={round(b, 3)}",
      xlabel='x',
      ylabel='x,y')
    ax.legend("s")
    ax.grid()
    sol = solve_ivp(f, [0, 10], [n, a, 0], args=(b, g), dense_output=True)
    z = sol.sol(t)
    line = ax.plot(t, z.T)
    return line

f_animation = animation.FuncAnimation(fig, 
                                      animate, 
                                      frames=np.linspace(0, 0.05, 100),
                                      interval = 500,
                                      repeat = False)

#save gif
/*f_animation.save('recovery.gif',
                 writer='imagemagick', 
                 fps=30)*/
