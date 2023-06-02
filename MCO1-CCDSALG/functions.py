# string, cnt(start 0), list of strings, size of string
def divideString(str, strList, strSize):
    for index in range(0, len(str)):
        strList.append([index, str])
        str = str[1::]


def printList(strList):
    for key in range(0, len(strList)):
        print(f"[{strList[key][0]}]: {strList[key][1]}")
