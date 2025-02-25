def can_form_interleaving(A, B, C):
    len_a, len_b = len(A), len(B)
    if len(C) != len_a + len_b:
        return False
    
    dp = [[False] * (len_b + 1) for _ in range(len_a + 1)]
    dp[0][0] = True
    
    for i in range(1, len_a + 1):
        dp[i][0] = dp[i-1][0] and A[i-1] == C[i-1]
    
    for j in range(1, len_b + 1):
        dp[0][j] = dp[0][j-1] and B[j-1] == C[j-1]
    
    for i in range(1, len_a + 1):
        for j in range(1, len_b + 1):
            dp[i][j] = (dp[i-1][j] and A[i-1] == C[i+j-1]) or (dp[i][j-1] and B[j-1] == C[i+j-1])
    
    return dp[len_a][len_b]

def main():
    n = int(input().strip())
    for case_num in range(1, n + 1):
        A, B, C = input().strip().split()
        result = "yes" if can_form_interleaving(A, B, C) else "no"
        print(f"Data set {case_num}: {result}")

if __name__ == "__main__":
    main()
