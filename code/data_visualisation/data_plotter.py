import numpy as np
from matplotlib import pyplot as plt


def main():
    data1=np.genfromtxt('mprofile_20200122120337.dat')
    data2=np.genfromtxt('mprofile_20200122120353.dat')


    X=data1[:,2]-data1[1,2]
    Y=data1[:,1]

    plt.plot(X,Y, linewidth=2.0)

    X2=data2[:,2]-data2[1,2]
    Y2=data2[:,1]

    plt.plot(X2,Y2, linewidth=2.0)

    plt.title('Memory_clearer vs storing nodes Breath first 6x6_1')
    plt.ylabel('Used memory [MB]')
    plt.xlabel('Time [s]')
    plt.show()

if __name__ == "__main__":
    main()
