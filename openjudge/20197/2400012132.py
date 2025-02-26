def cut_the_square(a,b,count=0):
    count+=1
    if a==b:
        return count
    else:
        return cut_the_square(min(a,b-a),max(a,b-a),count)

N,M=map(int,input().split())
print(cut_the_square(min(N,M),max(N,M)))

#注意如果没有切干净，那么else中应该return原函数以实现递归。