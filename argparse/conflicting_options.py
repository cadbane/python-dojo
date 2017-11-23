import argparse

parser = argparse.ArgumentParser(description='-v or -q :)')

group = parser.add_mutually_exclusive_group()
group.add_argument('-v', '--verbose', action='store_true')
group.add_argument('-q', '--quiet', action='store_true')

args = parser.parse_args()

print('verbose:', args.verbose)
print('quiet:', args.quiet)