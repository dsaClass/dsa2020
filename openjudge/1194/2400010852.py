from collections import Counter
n=int(input())
for case in range(1,n+1):
    s1,s2,s3=input().split()
    len1,len2=len(s1),len(s2)
    len3=len(s3)
    if len3!=len1+len2 or Counter(s1+s2)!=Counter(s3):
        print(f"Data set {case}: no")
        continue
    dp=[False]*(len2+1)
    dp[0]=True
    for j in range(1,len2+1):
        dp[j]=dp[j-1] and(s2[j-1]==s3[j-1])
    for i in range(1,len1+1):
        dp[0]=dp[0] and(s1[i-1]==s3[i-1])
        for j in range(1,len2+1):
            pos=i+j-1
            from_s1=(s1[i-1]==s3[pos])and dp[j]
            from_s2=(s2[j-1]==s3[pos])and dp[j-1]
            dp[j]=from_s1 or from_s2
    print(f"Data set {case}: {'yes' if dp[len2] else 'no'}")
