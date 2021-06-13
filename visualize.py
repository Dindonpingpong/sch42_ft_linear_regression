import matplotlib.pyplot as plt
import numpy as np
import argparse

THETA0 = 0
THETA1 = 0

def loadThetas():
    f = open("thethas.csv", "r")
    global THETA0
    global THETA1

    thethas = f.read().split(',')

    if (len(thethas) == 2):
        THETA0 = float(thethas[0])
        THETA1 = float(thethas[1])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
    description="Program that visualize results")
    parser.add_argument("subject", help="Visualize results", choices=['errors','data', 'model'])

    args = parser.parse_args()

    if (args.subject == 'errors'):
        data = np.genfromtxt('errors.csv')
        plt.plot([i for i in range(len(data))], data)
    elif (args.subject == 'data'):
        data = np.genfromtxt('data.csv',delimiter=',')
        loadThetas()
        plt.plot(data[0:,0], data[0:,1], 'o')
    else:
        data = np.genfromtxt('data.csv',delimiter=',')
        loadThetas()
        plt.plot(data[0:,0], data[0:,1], 'o')
        plt.plot(data[0:,0],data[0:,0] * THETA1 + THETA0, "r")
    
    plt.show()