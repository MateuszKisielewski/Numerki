import numpy as np
import matplotlib.pyplot as plt

def wykres(f, a, b, wynik):
    x = np.linspace(a, b, 2000)
    y = f(x)
    plt.plot(x, y)
    plt.plot(wynik, f(wynik), marker = 'o', color = 'r', markersize=8)
    plt.title("Wykres wybranej funkcji")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid()
    plt.show()