import numpy as np
import matplotlib.pyplot as plt
from scipy import special

t = np.arange(0, 20.0, 0.1)

plt.plot(t, special.spherical_jn(1, t), label="n1")
plt.plot(t, special.spherical_jn(2, t), label="n2")

plt.xticks(np.arange(0,21,1))
plt.xlabel('z')
plt.ylabel('jn(z)')
plt.title('Beselova Funkcija')

plt.grid()
plt.legend()
plt.show()
