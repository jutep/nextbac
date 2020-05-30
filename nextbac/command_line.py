import nextbac.start as start
import argparse
import sys


# entry point of program
# here should also be my cli implementation stuff
def main(args=sys.argv):
    # creating parser
    myParser = argparse.ArgumentParser()

    # adding arguments
    myParser.add_argument('-r', '--remove', nargs="*")
    myParser.add_argument('-s', action='store_true')

    # getting arguments
    args = vars(myParser.parse_args())

    # deciding what to do with args
    # removing pictures
    if (args['remove']):
        print('remove not configured yet sry')
    # ststistics mode
    elif (args['s']):
        print('sry statistics not implemented yet')
    # default mode to backup the server to local
    else:
        start.backupStart()

