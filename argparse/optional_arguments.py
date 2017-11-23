import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-v', '--verbose', help='increase output verbosity', action='store_true')
parser.add_argument('-s', help='super level', type=int, choices=[1,2,3])
parser.add_argument('-w', help='weird level', action='count', default=3) # -w -w -w ; ret 6
args = parser.parse_args()

if args.verbose:
    print('verbosity turned on')

super_map = {
    1: ':|',
    2: ':)',
    3: ':D'
}

if args.s:
    print('Super level: {}'.format(super_map[args.s]))

if args.w:
    print(args.w)