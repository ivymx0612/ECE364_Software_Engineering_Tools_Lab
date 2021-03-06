#! /usr/bin/env python3.4
#
#$Author: ee364a07 $
#$Date: 2016-09-27 11:07:33 -0400 (Tue, 27 Sep 2016) $
#$Revision: 94049 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/F16/students/ee364a07/Lab05/practical1.py $
#$Id: practical1.py 94049 2016-09-27 15:07:33Z ee364a07 $

def isValidOutput(fileName):
    newsud = []
    with open (fileName, 'r') as input:
        allline = input.readlines()
        for line in allline:
            line = list(line)
            line = line[0:9]
            newsud.append(line)
    result = True
    for item in newsud:
        item = set(item)
        item = list(item)
        item.sort()
        if len(item) != 9:
            result = False
        elif (item[0] != "1") or (item[8] != "9"):
            result = False
    count = 0
    while count < 9:
        newlist = []
        for item in newsud:
            newlist.append(item[count])
        newlist = set(newlist)
        newlist = list(newlist)
        newlist.sort()
        if len(newlist) != 9:
            result = False
        elif (newlist[0] != "1") or (newlist[8] != "9"):
            result = False
        count = count + 1
    return result


def isColumnPuzzle(fileName):
    newsud = []
    with open (fileName, 'r') as input:
        allline = input.readlines()
        for line in allline:
            line = list(line)
            line = line[0:9]
            newsud.append(line)
    if ['.', '.', '.', '.', '.', '.', '.', '.', '.'] in newsud:
        return False
    else:
        return True

def solvePuzzle(sourceFileName, targetFileName):
    col = isColumnPuzzle(sourceFileName)
    newsud = []
    with open (sourceFileName, 'r') as input:
        allline = input.readlines()
        for line in allline:
            line = list(line)
            line = line[0:9]
            newsud.append(line)
    if col == True:
        for item in newsud:
            add = 0
            for num in ['1','2','3','4','5','6','7','8','9']:
                if num not in item:
                    add = num
            addindex = item.index('.')
            item[addindex] = add
        count = 1
        with open (targetFileName, 'w') as output:
            for item in newsud:
                for num in item:
                    output.write(num)
                if count < 9:
                    output.write('\n')
                count = count + 1
    else:
        finallist = []
        count = 0
        while count < 9:
            newlist = []
            for item in newsud:
                newlist.append(item[count])
            finallist.append(newlist)
            count = count + 1
        for item in finallist:
            add = 0
            for num in ['1','2','3','4','5','6','7','8','9']:
                if num not in item:
                    add = num
            addindex = item.index('.')
            item[addindex] = add
        count = 0
        resultlist = []
        while count < 9:
            newlist = []
            for item in finallist:
                newlist.append(item[count])
            resultlist.append(newlist)
            count = count + 1
        count = 1
        with open (targetFileName, 'w') as output:
            for item in resultlist:
                for num in item:
                    output.write(num)
                if count < 9:
                    output.write('\n')
                count = count + 1

def getCallersOf(phoneNumber):
    people = {}
    result = []
    with open ("People.txt") as input:
        allline = input.readlines()
        allline = allline[2:]
        for line in allline:
            line = line.split()
            name = line[0] + ' ' + line[1]
            ext = line[3]
            ext = ext[1:]
            people[ext] = name
    with open ("ActivityList.txt", 'r') as input:
        allline = input.readlines()
        allline = allline[2:]
        for line in allline:
            line = line.split()
            callto = line[1]
            if callto == phoneNumber:
                callfrom = line[0]
                callfrom = callfrom.split('-')
                callfrom = callfrom[2]
                result.append(people[callfrom])
    result = set(result)
    result = list(result)
    result.sort()
    return result

def getCallActivity():
    result = {}
    people = {}
    with open ("People.txt") as input:
        allline = input.readlines()
        allline = allline[2:]
        for line in allline:
            line = line.split()
            name = line[0] + ' ' + line[1]
            ext = line[3]
            ext = ext[1:]
            people[ext] = name
    with open ("ActivityList.txt", 'r') as input:
        allline = input.readlines()
        allline = allline[2:]
        for line in allline:
            line = line.split()
            callfrom = line[0]
            calltime = line[2]
            callfrom = callfrom.split('-')
            callfrom = callfrom[2]
            name = people[callfrom]
            calltime = list(calltime)
            callhour = 0
            callmin = int(calltime[0] + calltime[1])
            callsec = int(calltime[3] + calltime[4])
            if name in result:
                old = result[name]
                old[0] = old[0] + 1
                old[1] = old[1] + callhour
                old[2] = old[2] + callmin
                old[3] = old[3] + callsec
                result[name] = old
            else:
                result[name] = [1, callhour, callmin, callsec]
    final = {}
    for key, value in result.items():
        times = value[0]
        min = int(value[2]) + int(value[3] / 60)
        sec = int(value[3] % 60)
        hour = int(value[1]) + int(min / 60)
        min = int(min % 60)
        final[key] = (times, "{0:02d}:{1:02d}:{2:02d}".format(hour, min, sec))
    return final



if __name__ == "__main__":
    result = isValidOutput("valid.sud")
    print(result)

    result = isColumnPuzzle("open1.sud")
    print(result)

    solvePuzzle("open1.sud", "result1.sud")

    result = getCallersOf('707-825-5871')
    print(result)

    result = getCallActivity()
    print(result["Edwards, Rachel"])