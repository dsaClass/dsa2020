#c的优化
#源代码中用了for循环来更新列表中的每个元素，优化后使用列表生成式
#更新元素时直接对每个元素进行(x+i)%65535操作，避免判断是否超过65535
#q的优化
#原代码将每个元素转化为二进制字符串来检验第i位是否非零，优化后使用>>运算将第i位挪到最低位，然后&1判断是否非0
#用sum结合生成器表达式来统计符合条件的元素个数
n, m = map(int, input().split())
num_list = list(map(int, input().split()))

for _ in range(m):
    operation, i = input().split()
    i = int(i)
    
    if operation == "C":
        num_list = [(x + i) % 65536 for x in num_list]
    elif operation == "Q":
        count = sum(1 for x in num_list if(x >> i) & 1)
        print(count)
