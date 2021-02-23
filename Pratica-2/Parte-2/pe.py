from os import listdir
from os.path import isfile, join
import re
import argparse
import pefile

def getArguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--path", help="Caminho dos XMLs", default="./")
    return parser.parse_args()

def getFiles(path):
    onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
    if ('pe.py' in onlyfiles):
        onlyfiles.remove('pe.py')
    regex = re.compile('.*.exe')
    onlyExes = [i for i in onlyfiles if regex.match(i)]

    onlyExes.sort()

    return onlyExes

if __name__ == '__main__':
    arguments = getArguments()
    files = getFiles(arguments.path)
    # print (files)
    # exit()
    # files = './calc.exe'
    for f in files:
        pe = pefile.PE(f)
        for section in pe.sections:
            print(section.Name.decode('utf-8'))