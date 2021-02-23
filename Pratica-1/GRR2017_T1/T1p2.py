import sys
import re

def getFiles():
    community = open(sys.argv[1])
    sid = open(sys.argv[2])

    return community, sid

def getAvaliableProtocols():
    avaliableProtocols = {
        'ip': 0,
        'tcp': 1,
        'udp': 2,
        'icmp': 3
    }

    return avaliableProtocols

def splitLine(line):
    splitedLine = line.split(" ")

    return splitedLine

# aqui tem algumas linhas que não tem o # no começo isso é tratado pelo if
def getProtocol(splitedLine, avaliableProtocols):
    if (splitedLine[2] in avaliableProtocols):
        return avaliableProtocols[splitedLine[2]]
    return avaliableProtocols[splitedLine[1]]

def getPort(line):
    splitedLine = line.split(' -> ')
    port = splitedLine[1].split(' ')[1]
    
    return port

#crio um dicionario de mensagens sid
def getSidMessages(sid):
    messages = {}
    for line in sid:
        splitedLines = line.split('||')
        code = splitedLines[0]
        message = splitedLines[1]
        messages[code.strip()] = message.strip()
    return messages

def getMessage(sidMessages, line):
    sid = re.search("(sid:)([0-9]+)",line)
    sid = sid[2]

    return sidMessages[sid]

if __name__ == "__main__":

    community, sid = getFiles()
    avaliableProtocols = getAvaliableProtocols()
    try:
        sidMessages = getSidMessages(sid)
    except:
        print('sid não está no formato adequado')
        exit(1)
    newFile = open('T1p2.txt', 'w+')
    for line in community:
        try:
            splitedLine = splitLine(line)
            protocol = getProtocol(splitedLine, avaliableProtocols)
            port = getPort(line)
            message = getMessage(sidMessages, line)
            newFile.write("{},{},{}\n".format(protocol, port, message))
        except:
            pass