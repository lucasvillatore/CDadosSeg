import sys

def getFile():
    file = open(sys.argv[1])
    
    return file

def splitContent(line):
    splitedLine = line.split(":", 1)
    return splitedLine[0]

def removePUA(line):
    splitedLine = line.split(".")
    splitedLine.pop(0)

    return splitedLine

def splitLastColumn(line):
    splitedLine = line[2].split("-", 2)

    line.pop()

    # no dataset tem por exemplo Win.Adware.Slimware-6535193-1
    # ele tem 2 números separados por " - ", esse é o tratamento pra pegar o valor correto
    if (len(splitedLine) == 3):
        line.append(splitedLine[0] + "-" + splitedLine[1])
        line.append(splitedLine[2])
    else:
        line.append(splitedLine[0])
        line.append(splitedLine[1])
    return line

if __name__ == '__main__':
    file = getFile()
    groupedInformation = {}

    newFile = open("T1p1b.txt", "w+")
    for line in file:
        try:
            importantInformation = splitContent(line)
            lineWithOutPua = removePUA(importantInformation)
            definitiveLine = splitLastColumn(lineWithOutPua)

            newFile.write(",".join(definitiveLine) + "\n")
        except:
            pass