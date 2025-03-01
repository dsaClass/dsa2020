def notRepeatIterm(string):
    countNumber = {}
    for s in string:
        if s in countNumber:
            countNumber[s] += 1
        else:
            countNumber[s] = 1
    found = False
    if found == False:
        for key,value in countNumber.items() :
            if value == 1:
                found = True
                return string.index(key)
    if found == False:
        return -1

string=input()
print(notRepeatIterm(string))