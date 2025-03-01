import sys
dic=[0 for _ in range(26)]
str=input()
for i in range(len(str)):
    dic[ord(str[i])-97]+=1
for i in range(len(str)):
    if dic[ord(str[i])-97]==1:
        print(i)
        sys.exit()

print(-1)
