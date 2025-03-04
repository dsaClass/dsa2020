def Sierpinski_Fractal(n):
    if n == 1:
        list1=[' /\\ ','/__\\']
        return list1
    else:
        listlast = Sierpinski_Fractal(n-1)
        listcurrent=[]
        for i in listlast:
            listcurrent.append(' '*2**(n-1)   +  i  +' '*2**(n-1))
        for i in range(len(listlast)):
            listcurrent.append(listlast[i]  + listlast[i])
        return listcurrent
result=[]
n=int(input())
while n!=0:
    x=Sierpinski_Fractal(n)
    result.append(x)
    n=int(input())
for i in range(len(result)):
    if i < len(result)-1:
        for j in result[i]:
            print(j)
        print('')
    else:
        for j in result[i]:
            print(j)