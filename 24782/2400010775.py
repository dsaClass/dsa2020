s=input()

def imrg(s):
    if len(s)<3:
        return s
    else:
        i=0
        bo=0
        while i<=len(s)-3:
            if s[i:i+3]=='PKU':
                s=s[:i]+s[i+3:]
                bo=1
            else:
                i=i+1
        if bo==1:
            return imrg(s) 
        else:
            return s

print(imrg(s))