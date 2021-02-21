from os import listdir
from os.path import isfile, join
import re
import xmltodict
import json

def getFiles():
    onlyfiles = [f for f in listdir('./') if isfile(join('./', f))]
    if ('apk.py' in onlyfiles):
        onlyfiles.remove('apk.py')
    regex = re.compile('.*.xml')
    onlyImages = [i for i in onlyfiles if regex.match(i)]

    onlyImages.sort()

    return onlyImages

def fileXmlToDict(file):
    content = file.read()

    return xmltodict.parse(content)

def getPermissions(file):
    permissions = []
    try:
        for android in file['manifest']['uses-permission']:
            permission = android["@android:name"].split(".")

            permissions.append(permission.pop())
    except:
        pass
    return permissions

def getApkName(apk):
    _, apkNameXml = apk.split("_", 2)
    apkName, _ = apkNameXml.split(".", 2)

    return apkName

def printPermissions(apk, permissions):

    apkName = getApkName(apk)
    print("{}:\n".format(apkName, permissions))
    print(permissions)
    print("\n")

if __name__ == '__main__':
    files = getFiles()

    androidApks = {}

    for apk in files:
        file = open(apk, "r")
        fileDict = fileXmlToDict(file)
        androidApks[apk] = {}
        androidApks[apk] = getPermissions(fileDict)

    print("############ Permissões por APK ############\n")
    for androidApk in androidApks:
        printPermissions(androidApk, androidApks[androidApk])