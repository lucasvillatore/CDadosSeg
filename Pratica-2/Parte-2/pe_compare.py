import sys
import pefile


def getSections(file):
    sections = []

    pe = pefile.PE(file)
    for section in pe.sections:
        sectionName = section.Name.decode('utf-8').split("\x00")
        sections.append(sectionName[0])

    return sections

def printCommonSections(first, second):
    commonSections = []
    for section in first:
        if (section in second):
            commonSections.append(section)

    print(commonSections)

def printUniqueSections(binary, binaryToCompare):
    uniqueSections = []
    for section in binary:
        if (section not in binaryToCompare):
            uniqueSections.append(section)
    
    print(uniqueSections)

if __name__ == "__main__":
    first_pe = sys.argv[1]
    second_pe = sys.argv[2]

    sections_first_pe = getSections(first_pe)
    sections_second_pe = getSections(second_pe)

    print("######## Seções comuns entre os binários {} e {} ########\n".format(first_pe, second_pe))
    printCommonSections(sections_first_pe, sections_second_pe)

    print("\n")
    print("######## Seções únicas de {} ########\n".format(first_pe))
    printUniqueSections(sections_first_pe, sections_second_pe)
    
    print("\n")
    print("######## Seções únicas de {} ########\n".format(second_pe))
    printUniqueSections(sections_second_pe, sections_first_pe)
    print("\n")