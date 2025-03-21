import heapq
import sys

def assign_cows() :
    n=int(sys.stdin.readline())
    cows=[]
    for i in range(n) :
        a,b=map(int,sys.stdin.readline().split())
        cows.append((a,b,i))
    cows.sort()
    
    stalls=[]
    assignment=[0]*n
    stall_id=0
    for a,b,idx in cows :
        if stalls and stalls[0][0]<a :
            end_time,sid=heapq.heappop(stalls)
            assignment[idx]=sid
            heapq.heappush(stalls,(b,sid))
        else:
            stall_id+=1
            assignment[idx]=stall_id
            heapq.heappush(stalls,(b,stall_id))
    
    print(stall_id)
    for a in assignment :
        print(a)

assign_cows()