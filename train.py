
from argparse import ArgumentParser
from numpy import array, sum, isnan, genfromtxt
from utils import FILE_WITH_THETHAS, FILE_WITH_MSE


def init_args_parser() -> ArgumentParser:
    parser = ArgumentParser(
        description="Program that train prediction model")
    parser.add_argument("dataset", type=str, help="Path to file with data")
    parser.add_argument("learning_rate", type=float, help="Learning rate")
    parser.add_argument("number_epoch", type=int, help="Number of epoch")

    return parser


def get_dataset(path: str) -> list[array]:
    raw_data = genfromtxt(path, delimiter=',')

    x = raw_data[1:, 0]
    y = raw_data[1:, 1]
 
    if (isnan(sum(x)) or isnan(sum(y))):
        print("Invalid data in dataset")
        exit(1)

    if (len(x) < 10 or len(y) < 10):
        print("""
            Too low number of records(
            Increase your number of row to get more efficient linear model.
        """)

    return x, y


if __name__ == "__main__":
    theta0, theta1 = 0, 0
    args = init_args_parser().parse_args()
    x_train, y_train = get_dataset(args.dataset)

    x_train /= 1000
    y_train /= 1000

    errors = []

    for i in range(args.number_epoch):
        y_predict = theta0 + (theta1 * x_train)

        sum0 = (y_predict - y_train).mean()
        sum1 = ((y_predict - y_train) * x_train).mean()

        errors.append(((y_predict - y_train) ** 2).mean())

        tmp_theta0 = args.learning_rate * sum0
        tmp_theta1 = args.learning_rate * sum1

        theta0 -= tmp_theta0
        theta1 -= tmp_theta1

    f = open(FILE_WITH_THETHAS, "w")

    f.write(f'{theta0 * 1000},{theta1}')

    f.close()

    f2 = open(FILE_WITH_MSE, "w")

    for error in errors:
        f2.write(f'{error}\n')

    f2.close()
