import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

fig, ax1 = plt.subplots(1,1)

def animate(i,argu):
    print(i, argu)

    #graph_data = open('example.txt','r').read()
    graph_data = "1, 1 \n 2, 4 \n 3, 9 \n 4, 16 \n"
    lines = graph_data.split('\n')
    xs = []
    ys = []
    for line in lines:
        if len(line) > 1:
            x, y = line.split(',')
            xs.append(float(x))
            ys.append(float(y)+np.sin(2.*np.pi*i/10))
        ax1.clear()
        ax1.plot(xs, ys)
        plt.grid()

ani = animation.FuncAnimation(fig, animate, fargs=[5],interval = 100)
plt.show()