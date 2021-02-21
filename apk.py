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
    print("{}: {}\n".format(apk, permissions))

def getListOfUniquePermissions(androidApks):
    pass

def getListOfRepeatedPermissions(androidApks):
    androidPermissions = {}
    for androidApk in androidApks:
        for apkPermission in androidApks[androidApk]:
            try:
                if (androidApk not in androidPermissions[apkPermission]):
                    androidPermissions[apkPermission].append(androidApk)
            except:
                androidPermissions[apkPermission] = [androidApk]
    return androidPermissions

def getListOfRepeatedPermissionsInAllApks(repeteadPermissions, apks):
    numberOfApks = len(apks)

    permissionRepeteadInAllApks = []
    for permission in repeteadPermissions:
        if (len(repeteadPermissions[permission]) == numberOfApks):
            permissionRepeteadInAllApks.append(permission)

    return permissionRepeteadInAllApks


def getListOfUniquePermissionsInAllApks(repeteadPermissions):
    permissionUniqueInAllApks = {}
    for permission in repeteadPermissions:
        if (len(repeteadPermissions[permission]) == 1):
            permissionUniqueInAllApks[repeteadPermissions[permission].pop()] = permission

    return permissionUniqueInAllApks


if __name__ == '__main__':
    files = getFiles()

    androidApks = {}

    for apk in files:
        file = open(apk, "r")
        fileDict = fileXmlToDict(file)
        
        apkName = getApkName(apk)
        androidApks[apkName] = {}
        androidApks[apkName] = getPermissions(fileDict)

    print("############ Permissões por APK ############\n")
    for androidApk in androidApks:
        printPermissions(androidApk, androidApks[androidApk])


    print("############ Permissões únicas das APKS ############\n")
    repeteadPermissions = getListOfRepeatedPermissions(androidApks)
    androidApksPermissionsUnique = getListOfUniquePermissionsInAllApks(repeteadPermissions)
    for androidApk in androidApksPermissionsUnique:
        printPermissions(androidApk, androidApksPermissionsUnique[androidApk])


    print("############ Permissões comuns das APKS ############\n")
    repeteadPermissions = getListOfRepeatedPermissions(androidApks)
    print(getListOfRepeatedPermissionsInAllApks(repeteadPermissions, files))