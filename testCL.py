import argparse

def simplePrint(a, b):
	print a, b


parser = argparse.ArgumentParser(description='prints two arguments')
parser.add_argument('A')
parser.add_argument('B')
args = parser.parse_args()
simplePrint(getattr(args, 'A'), getattr(args, 'B'))
