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

def getSections(file):
    sections = []

    pe = pefile.PE(f)
    for section in pe.sections:
        sections.append(section)

    return sections

def printSectionFronFiles(filesSectionsDict):
    print ("######## SEÇÕES ########\n")
    for binary in filesSectionsDict:
        executableSections = getExecutables(filesSectionsDict[binary])
        print("Binary: {} - Sections : {}\n".format(binary, executableSections))

def getExecutables(sections):
    isExecutable = []
    for section in sections:
        if checkIfIsExecutable(section):
            sectionName = section.Name.decode('utf-8').split("\x00")
            isExecutable.append(sectionName[0])

    return isExecutable

def checkIfIsExecutable(section):
    characteristics = getattr(section, 'Characteristics')
    if characteristics & 0x00000020 > 0 or characteristics & 0x20000000 > 0:
        return True
    return False

if __name__ == '__main__':
    arguments = getArguments()
    files = getFiles(arguments.path)
    
    filesSectionsDict = {}
    for f in files:
        pe = pefile.PE(f)
        sections = getSections(f)
        filesSectionsDict[f] = {}
        filesSectionsDict[f] = sections

    printSectionFronFiles(filesSectionsDict)
    # print(filesSectionsDict)