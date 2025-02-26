s=input()
s_list=list(s)
s_dict={}
for char in s:
    if char in s_dict:
        s_dict[char]+=1
    else:
        s_dict[char]=1
s_list_keys=list(s_dict.keys())
s_list_values=list(s_dict.values())

myindex=-1
for value in s_list_values:
    if value==1:
        myindex=s_list.index(s_list_keys[s_list_values.index(value)])
        break
print(myindex)
#注意看清楚是下标还是第几个。