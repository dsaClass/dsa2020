num_list=list(map(int,str(input())))
for i in range(len(num_list)):
    if num_list[i]==2:
        num_list[i]+=1
        break
print(int(''.join(map(str,num_list))))

#注意一种不可行的写法：
#   num_list=list(map(int,str(input())))
#   for i in num_list:
#       if i==2:
#           i+=1
#           break
#   print(int(''.join(map(str,num_list))))
#for里面的i实际上是一个新的变量，只不过映射了num_list中对应位置的量，只是修改i并没有实现对原列表的修改。

#另外在这里也可以学join的用法，将数字列表以字符形式连接，最后转化为数字。
#join句点前面的引号标识了用什么东西间隔连接。