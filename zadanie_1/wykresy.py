import numpy as np
import matplotlib.pyplot as plt

def wykres(f, a, b):
    x = np.linspace(a, b, 2000)
    y = f(x)
    plt.plot(x, y)
    plt.title("Wykres wybranej funkcji")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid()
    plt.show()