import argparse

parser = argparse.ArgumentParser(
    description="Program that train prediction model")
parser.add_argument("-v", help="Visualize results", action='store_true')

args = parser.parse_args()

print(args.v)
