from numpy import *
import re
# load text one line at a time..
def loadstr(filename,converter=str):
    with open(filename) as fd:
        return [converter(c.strip()) for c in fd.readlines()]

# load text one line at a time, the numbers are comma separates per line..
def loadint(filename,converter=str):
    with open(filename) as fd:
        integers = [map(int, converter(c.strip()).split(',')) for c in fd.readlines()]
        return integers

# write text one line at a time..
# forming a template..
def writestr(filename,texts):
    with open(filename, 'w') as outfile:
        for i in range(len(texts)):
            line = str(texts[i]) + '\n'
            #line = re.sub('[!@#$]', '', line)
            #line.rstrip()
            #line = line + '\n'
            outfile.write(line)

def loadcsv(filename, skip):
    output = []
    with open(filename) as fr:
        if skip == 1:
            next(fr)
        for line in fr:
            output.append(map(float, line.split(',')))
    return array(output)
