while True:
    n=int(input())
    if n==0:
        break
    a=list(map(int,input().split()))
    def mergesort(a):
        ans=i=j=s=0
        if len(a)<=1:
            return 0
        left,right=a[:len(a)//2],a[len(a)//2:]
        ans+=mergesort(left)
        ans+=mergesort(right)
        a.clear()
        while i<len(left) and j<len(right):
            if left[i]<=right[j]:
                a.append(left[i])
                s+=j
                i+=1
            else:
                a.append(right[j])
                j+=1
        if j<len(right):
            a+=right[j:]
        while i<len(left):
            a.append(left[i])
            s+=j
            i+=1
        return ans+s
    print(mergesort(a))
