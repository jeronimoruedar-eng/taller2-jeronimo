print("Hello World!")
x = 0.5

def raiz_cuadrada(x:float) -> float:
    return x**0.5

print("La raíz cuadrada de 1000 es: " + str(raiz_cuadrada(1000)))
#--------------------------------------------------
#Grafico 1
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
#--------------------------------------------------
#Gráfico 2

import matplotlib.pyplot as plt
import numpy as np

np.random.seed(1234)

n = 100
x = np.random.rand(n)
y = np.random.rand(n)
z = x**2
w = np.pi*np.random.randint(0,10,n)**2

plt.scatter(x, y, c=z) 
plt.scatter(x, x, s=w, alpha=0.6) 
plt.show()

#--------------------------------------------------
#Gráfico 3

import matplotlib.pyplot as plt
import numpy as np
np.random.seed(40)
fig, ax = plt.subplots()
ax.plot(np.random.standard_normal(1000).cumsum(),label="TLA")
ax.plot(np.random.standard_normal(1000).cumsum(),label="APL")
ax.plot(np.random.standard_normal(1000).cumsum(),label="MSF")
ax.legend() #loc="upper right"
plt.show()