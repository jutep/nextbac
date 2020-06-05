import nextbac.start as start
import argparse
import sys
import select


def main(args=sys.argv):
    removePics = {}
    if len(args) > 2:
        removePics = [line[:-1] for line in sys.stdin if line[-4:-1] == 'jpg']

    # creating parser
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', action='store_true')
    parser.add_argument('-rl', action='store_true')
    parser.add_argument('-rs', action='store_true')
    parser.add_argument('-s', action='store_true')

    # parsing args
    args = vars(parser.parse_args())

    if removePics:
        # remove in server and backup
        if (args['r']):
            start.remove(removePics)
        # remove in backup only
        elif (args['rl']):
            print('remove local not implemented yet')
        # remove on server only
        elif (args['rs']):
            print('remove server not implemented yet')
        else:
            raise Exception('no remove mode specified use -r; -rl; -rs')
    else:
        # ststistics mode
        if (args['s']):
            print('sry statistics not implemented yet')
        else:
            for flagExists in args.values():
                if flagExists:
                    raise Exception('Wrong configuration of flags and input')
            start.backup()
