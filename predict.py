import argparse

from utils import loadThetas

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Program that predict price of car using the linear regression hypothesis")
    parser.add_argument("milleage", type=int, help="Car milleage")

    args = parser.parse_args()

    theta0, theta1 = loadThetas()

    print("Your estimate car price is", theta0 + args.milleage * theta1)
