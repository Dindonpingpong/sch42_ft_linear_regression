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
        description="Program that predict price of car using the linear regression hypothesis")
    parser.add_argument("milleage", type=int, help="Car milleage")

    args = parser.parse_args()

    loadThetas()

    print("Your estimate car price is", THETA0 + args.milleage * THETA1)
