from os import listdir
from os.path import isfile, join
import re
import xmltodict
import json
import argparse

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

if __name__ == '__name__':
    arguments = getArguments()
    files = getFiles(arguments.path)

    