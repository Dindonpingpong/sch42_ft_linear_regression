from predict import THETA0, THETA1
import numpy as np
import argparse

THETA0 = 0
THETA1 = 0

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Program that train prediction model")
    parser.add_argument("learning_rate", type=float, help="Learning rate")
    parser.add_argument("number_epoch", type=int, help="Number of epoch")
    parser.add_argument("-v", help="Visualize results", action='store_true')

    args = parser.parse_args()

    data = np.genfromtxt('data.csv', delimiter=',')

    data = np.delete(data, (0), axis=0)

    x_train = data[0:, 0]
    y_train = data[0:, 1]

    x_train /= 1000

    errors = []

    for i in range(args.number_epoch):
        y_predict = THETA0 + (THETA1 * x_train)

        sum0 = (y_predict - y_train).mean()
        sum1 = ((y_predict - y_train) * x_train).mean()

        errors.append(((y_predict - y_train) ** 2).mean())
        tmp_theta0 = args.learning_rate * sum0
        tmp_theta1 = args.learning_rate * sum1

        THETA0 -= tmp_theta0
        THETA1 -= tmp_theta1

    f = open("thethas.csv", "w")
    f.write(f'{THETA0},{THETA1 / 1000}')
    f.close()

    f2 = open("errors.csv", "w")
    for error in errors:
        f2.write(f'{error}\n')
    f2.close
