def check(previous_queens,pos):
    for pos_ in previous_queens:
        if pos_[0]==pos[0] or pos_[1]==pos[1] or abs(pos_[0]-pos[0])==abs(pos_[1]-pos[1]):
            return False
    return True

def output(queens,n):
    queens.sort(key=lambda x: x[1])
    print('No. '+str(n))
    for i in range(8):
        print('0 '*queens[i][0]+'1 '+'0 '*(7-queens[i][0]))


count=0
def put_queen(previous_queens,i):
    global count
    for j in range(8):
        if check(previous_queens,(i,j)):
            if i < 7:
                put_queen(previous_queens+[(i,j)],i+1)
            else:
                count+=1
                output(previous_queens+[(i,j)],count)

put_queen([],0)