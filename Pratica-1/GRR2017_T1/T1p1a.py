import sys

def getFile():
    file = open(sys.argv[1])
    
    return file

def splitContent(line):
    splitedLine = line.split(":")

    return splitedLine

def getTypeAndFamily(line):
    splitedInformation = line.split(".")

    return splitedInformation

def getFamilyAndVariant(variant):
    family, variant = variant.split("-", 1)
    variant = variant.replace('\n', '')
    
    return family, variant

if __name__ == '__main__':
    file = getFile()
    groupedInformation = {}
    for line in file:
        typeFamilyVariant = splitContent(line)[2]
        splitedLine = getTypeAndFamily(typeFamilyVariant)
        try:
            typeInformation = splitedLine[1]
            familyVariant = splitedLine[2]

            family, variant = getFamilyAndVariant(familyVariant)

            #esse hadouken de if é para criar o dicionario com as familias e as variantes que foram encontradas
            if typeInformation in groupedInformation:
                if family in groupedInformation[typeInformation]:
                    if variant in groupedInformation[typeInformation][family]:
                        groupedInformation[typeInformation][family][variant] += 1
                    else:
                        groupedInformation[typeInformation][family][variant] = 1
                else:
                    groupedInformation[typeInformation][family] = {}
                    groupedInformation[typeInformation][family][variant] = 1
            else:
                groupedInformation[typeInformation] = {}
                groupedInformation[typeInformation][family] = {}
                groupedInformation[typeInformation][family][variant] = 1

        except:
            pass
    newFile = open("T1p1a.txt", "w+")
    contentFile = []

    #guardo num array as familias tipos e quantidade de variantes para poder ordernar
    for i in groupedInformation:
        for j in groupedInformation[i]:
            contentFile.append(i+"."+j+","+str(len(groupedInformation[i][j])))
    contentFile.sort()
    
    
    for line in contentFile:
        newFile.write(line + "\n")