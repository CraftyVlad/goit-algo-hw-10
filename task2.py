import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad


def f(x):
    return x**2


a = 0
b = 2
samples = 100000

x_random = np.random.uniform(a, b, samples)
monte_carlo = (b - a) * np.mean(f(x_random))

quad_result, error = quad(f, a, b)

print(f"monte Carlo result: {monte_carlo}")
print(f"quad result: {quad_result}")
print(f"difference: {abs(monte_carlo - quad_result)}")

x = np.linspace(-0.5, 2.5, 400)

fig, ax = plt.subplots()

ax.plot(x, f(x), "r", linewidth=2)

ix = np.linspace(a, b)
ax.fill_between(ix, f(ix), color="gray", alpha=0.3)

ax.axvline(a, color="gray", linestyle="--")
ax.axvline(b, color="gray", linestyle="--")

ax.set_xlim(-0.5, 2.5)
ax.set_ylim(0, 6.5)
ax.set_xlabel("x")
ax.set_ylabel("f(x)")
ax.set_title("integral of f(x) = x^2 from 0 to 2")

plt.grid()
plt.show()