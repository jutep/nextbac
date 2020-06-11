import nextbac.start as start
import argparse
import sys
import select


def main(args=sys.argv):
    # creating parser
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', action='store_true')

    # parsing args
    args = vars(parser.parse_args())

    if not sys.stdin.isatty():
        removePics = [line[:-1] for line in sys.stdin if line[-4:-1] == 'jpg']
        removePics = stripPics(removePics)
        if removePics:
            start.remove(removePics)
        else:
            print('You need to pipe an picture to remove it')
    else:
        # ststistics mode
        if (args['s']):
            print('sry statistics not implemented yet')
        else:
            for flagExists in args.values():
                if flagExists:
                    raise Exception('Wrong configuration of flags and input')
            start.backup()


# stripping pictures if the pipe to nextbac is
# like: [year/month/picName.jpg]
# returns: [picName.jpg]
def stripPics(removePics):
    for index, picName in enumerate(removePics):
        if picName[0] != "I":
            copyPic = ""
            for counter, char in enumerate(picName):
                if char == "/":
                    copyPic = picName[counter+1:]
            removePics[index] = copyPic
    return removePics
