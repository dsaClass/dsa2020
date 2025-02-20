def count(s1, s2, s3):
    a = {}
    letters = 'ABCDE'
    def transfer(s):
        result = 0
        for i in s:
            if i not in a:
                return -1
            result = result * 10 + a[i] 
        if s and a[s[0]] == 0 and len(s) > 1:
            return -1
        return result
    def renum(position):
        if position == len(letters):
            n1, n2, n3 = transfer(s1), transfer(s2), transfer(s3)
            if n1 >= 0 and n2 >= 0 and n3 >= 0 and n1 + n2 == n3:
                print(f"{n1}+{n2}={n3}")
                return True
        else:
            for k in range(10):
                if k not in a.values(): 
                    a[letters[position]] = k
                    if renum(position + 1):
                        return True
                    del a[letters[position]]  
        return False
    return renum(0)
n = int(input())
for i in range(n):
   s1,s2,s3 = input().split()
   if not count(s1,s2,s3):
      print("No Solution")
