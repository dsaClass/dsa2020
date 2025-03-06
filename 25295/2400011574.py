n=int(input())
for _ in range(n):
    pro={}
    for i in range(3):
        s=list(input().split())
        if s[2]=='even':
            for k in range(4):
                pro[s[0][k]]=0
                pro[s[1][k]]=0
        elif s[2]=='up':
            for k in range(4):
                if s[0][k] in pro:
                    if pro[s[0][k]]!=0:
                        pro[s[0][k]]+=1
                else:
                    pro[s[0][k]]=1
                if s[1][k] in pro:
                    if pro[s[1][k]] != 0:
                        pro[s[1][k]]-=1
                else:
                    pro[s[1][k]]=-1
        elif s[2]=='down':
            for k in range(4):
                if s[0][k] in pro:
                    if pro[s[0][k]] != 0:
                        pro[s[0][k]]-=1
                else:
                    pro[s[0][k]]=-1
                if s[1][k] in pro:
                    if pro[s[1][k]] != 0:
                        pro[s[1][k]]+=1
                else:
                    pro[s[1][k]]=1
    max_key = max(pro, key=lambda k: abs(pro[k]))
    mass=pro[max_key]
    if mass<0:
        print(f'{max_key} is the counterfeit coin and it is light.')
    elif mass>0:
        print(f'{max_key} is the counterfeit coin and it is heavy.')
