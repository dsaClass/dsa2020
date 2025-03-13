class term:
    def __init__(self,coef,ex):
        self.coef,self.ex=coef,ex

    def __lt__(self,other):
        return self.ex <other.ex
    
    def __eq__(self, other):
        return self.ex ==other.ex
    
    def __add__(self, other):
        if self==other:
            return term(coef=self.coef+other.coef,ex=self.ex)
    
class polynomial:
    def __init__(self,lst):
        self.terms=[]
        while lst:
            ex=lst.pop()
            coef=lst.pop()
            self.terms.append(term(coef,ex))
        self.terms.sort()
        i=0
        while i <len(self.terms)-1:
            if self.terms[i]!=self.terms[i+1]:
                i+=1
            else:
                self.terms[i]+=self.terms[i+1]
                self.terms.pop(i+1)

    def __add__(self,other):
        result=polynomial([])
        m,n=len(self.terms),len(other.terms)
        i=j=0
        while i<m and j<n:
            if self.terms[i]==other.terms[j]:
                result.terms.append(self.terms[i]+other.terms[j])
                i+=1
                j+=1
            elif self.terms[i]<other.terms[j]:
                result.terms.append(self.terms[i])
                i+=1
            else:
                result.terms.append(other.terms[j])
                j+=1
        if i<m:
            result.terms+=self.terms[i:]
        if j<n:
            result.terms+=other.terms[j:]
        return result

    def __repr__(self):
        result=''
        for i in sorted(self.terms,reverse=True):
            if i.coef==0:
                continue
            result=result+f'[ {i.coef} {i.ex} ] '
        return result


if __name__=='__main__':
    n=int(input())
    for _ in range(n):
        lst=list(map(int,input().split()))
        lst.pop()
        lst.pop()
        p1=polynomial(lst)

        lst=list(map(int,input().split()))
        lst.pop()
        lst.pop()
        p2=polynomial(lst)
        print(p1+p2)
