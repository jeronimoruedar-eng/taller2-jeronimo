print("Hello World!")
x = 0.5

def raiz_cuadrada(x:float) -> float:
    return x**0.5

print("La raíz cuadrada de 1000 es: " + str(raiz_cuadrada(1000)))

import matplotlib.pyplot as plt
import numpy as np

np.random.seed(1234)

n = 200
x = np.random.rand(n)
y = np.random.rand(n)

plt.hist(x, bins=10, alpha=0.6, label="x")
plt.hist(y, bins=10, alpha=0.6, label="y")
plt.legend()
plt.show()

