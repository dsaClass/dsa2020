import sys

def find_pair_with_sum(n,arr,m) :
    seen=set()
    result=None
    
    for num in arr :
        complement=m-num
        if complement in seen :
            pair=(min(num,complement),max(num,complement))
            if result is None or pair<result :
                result=pair
        seen.add(num)
    
    if result :
        print(result[0],result[1])
    else :
        print("No")

def main() :
    input_data=sys.stdin.read().splitlines()
    n=int(input_data[0])
    arr=list(map(int,input_data[1].split()))
    m=int(input_data[2])
    
    find_pair_with_sum(n,arr,m)

if __name__=="__main__" :
    main()