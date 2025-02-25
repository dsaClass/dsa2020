import sys
def match(word):
    lst=[]
    i=0
    while i<len(word):
        if word[i]=='(' or word[i]=='[':
            lst.append(word[i])
        elif word[i]==')':
            if len(lst)==0 or lst[-1]!='(':
                return 0
            else:
                lst=lst[:-1]
        elif word[i] == ']':
            if len(lst) != 0 and lst[-1] == '[':
                lst=lst[:-1]
            else:
                return 0
        elif word[i] == '*':
            if i + 1 < len(word) and word[i + 1] == '/':
                if len(lst)!=0 and lst[-1]=='/*':
                    lst=lst[:-1]
                    i+=1
                else:return 0
            else:return 0
        elif word[i]=='/':
            if i+1<len(word) and word[i+1]=='*':
                lst.append('/*')
                i+=1
            else:return 0
        i+=1
    if (len(lst)==0):return 1
    else:return 0


for word in sys.stdin:
    s=word.strip()
    if match(s)==1:print('True')
    else:print('False')
