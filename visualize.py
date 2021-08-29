import matplotlib.pyplot as plt
import numpy as np
import argparse

from utils import loadThetas

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Program that visualize results")
    parser.add_argument("subject", help="Visualize results",
                        choices=['errors', 'data', 'model'])

    args = parser.parse_args()

    if (args.subject == 'errors'):
        data = np.genfromtxt('mse.csv')

        plt.plot([i for i in range(len(data))], data)
    else:
        data = np.genfromtxt('data.csv', delimiter=',')
        theta0, theta1 = loadThetas()

        plt.plot(data[0:, 0], data[0:, 1], 'o')

        if (args.subject == 'model'):
            plt.plot(data[0:, 0], data[0:, 0] * theta1 + theta0, "r")

    plt.show()
