FILE_WITH_THETHAS = "thethas.csv"
FILE_WITH_MSE = "mse.csv"

def loadThetas() -> list[int]:
    theta0 = 0
    theta1 = 0

    try:
        f = open(FILE_WITH_THETHAS, "r")

        thethas = f.read().split(',')

        if (len(thethas) == 2):
            theta0 = float(thethas[0])
            theta1 = float(thethas[1])

    finally:
        return theta0, theta1
