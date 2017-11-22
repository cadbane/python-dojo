import argparse

parser = argparse.ArgumentParser()
parser.add_argument('a', help='argument a', type=int)
parser.add_argument('b', help='argument b', type=int)
args = parser.parse_args()

a = args.a
b = args.b

print(f'{a}+{b}={a+b}')
print(f'{a}-{b}={a-b}')
