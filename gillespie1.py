import numpy as np
import matplotlib

matplotlib.use('tkagg')
import matplotlib.pyplot as plt
import random

from scipy.integrate import odeint

A = [1000]
B = [1000]
C = [1000]
D = [1000]

t = [0]

tend = 500

k1 = 0.5
k2 = 0.001

while t[-1] < tend:
    props = [k1 * A[-1] * B[-1], k2 * B[-1] ** 2 * C[-1]]
    prop_sum = sum(props)
    if prop_sum == 0:
        break
    tau = np.random.exponential(scale=1 / prop_sum)
    t.append(t[-1] + tau)
    rand = random.uniform(0, 1)
    if rand * prop_sum <= props[0]:
        A.append(A[-1] - 1)
        B.append(B[-1] - 1)
        C.append(C[-1] + 2)
        D.append(D[-1])
    elif props[0] < rand * prop_sum <= props[0] + props[1]:
        A.append(A[-1])
        B.append(B[-1] - 2)
        C.append(C[-1] - 1)
        D.append(D[-1] + 1)

A_plot, = plt.plot(t, A, label="$A$")
B_plot, = plt.plot(t, B, label="$B$")
C_plot, = plt.plot(t, C, label="$C$")
D_plot, = plt.plot(t, D, label="$D$")

# plt.legend(handles=[A_plot, B_plot, C_plot, D_plot])

plt.xlabel("$Time$")
plt.ylabel("$Abundance$")
# plt.show()

new_tend = t[-1]
y0 = [1000, 1000, 1000, 1000]
t = np.linspace(0, new_tend, num=1000)
params = [k1, k2]


def sim(variables, t, params):
    A = variables[0]
    B = variables[1]
    C = variables[2]
    D = variables[3]

    k1 = params[0]
    k2 = params[1]

    dAdt = -k1 * A * B
    dBdt = (-k1 * A * B) - (2 * k2 * B ** 2 * C)
    dCdt = (2 * k1 * A * B) - (k2 * B ** 2 * C)
    dDdt = k2 * B ** 2 * C

    return ([dAdt, dBdt, dCdt, dDdt])


y = odeint(sim, y0, t, args=(params,))

A_dplot, = plt.plot(t, y[:, 0], label="$A$ in differential equation")  # A
B_dplot, = plt.plot(t, y[:, 1], label="$B$ in differential equation")  # B
C_dplot, = plt.plot(t, y[:, 2], label="$C$ in differential equation")  # C
D_dplot, = plt.plot(t, y[:, 3], label="$D$ in differential equation")  # D

plt.legend(handles=[A_dplot, B_dplot, C_dplot, D_dplot, A_plot, B_plot, C_plot, D_plot])
# plt.show()

new_tend = t[-1]
y0 = [1000, 1000, 1000, 1000]
t = np.linspace(0, new_tend, num=1000)
params = [k1, k2]


def sim(variables, t, params):
    A = variables[0]
    B = variables[1]
    C = variables[2]
    D = variables[3]

    k1 = params[0]
    k2 = params[1]

    dAdt = -k1 * A * B
    dBdt = (-k1 * A * B) - (2 * k2 * B ** 2 * C)
    dCdt = (2 * k1 * A * B) - (k2 * B ** 2 * C)
    dDdt = k2 * B ** 2 * C

    return [dAdt, dBdt, dCdt, dDdt]


y = odeint(sim, y0, t, args=(params,))

A_dplot, = plt.plot(t, y[:, 0], label="$A$ in differential equation")  # A
B_dplot, = plt.plot(t, y[:, 1], label="$B$ in differential equation")  # B
C_dplot, = plt.plot(t, y[:, 2], label="$C$ in differential equation")  # C
D_dplot, = plt.plot(t, y[:, 3], label="$D$ in differential equation")  # D

plt.legend(handles=[A_dplot, B_dplot, C_dplot, D_dplot, A_plot, B_plot, C_plot, D_plot])
plt.show()
