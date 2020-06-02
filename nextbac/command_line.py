import nextbac.start as start
import argparse
import sys


# entry point of program
def main(args=sys.argv):
    # creating parser
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', '--remove', nargs="*")
    parser.add_argument('-s', action='store_true')
    args = vars(parser.parse_args())

    # remove mode
    if (args['remove']):
        print('remove not configured yet sry')
    # ststistics mode
    elif (args['s']):
        print('sry statistics not implemented yet')
    else:
        start.backupStart()

