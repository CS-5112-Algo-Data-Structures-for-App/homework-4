def find_max_form(strs, m, n):
    dp = []

    for _ in range(len(strs)+1):
        row = []

        for _ in range(m+1):
            inner_inner_list = [0] * (n+1)
            row.append(inner_inner_list)

        dp.append(row)
    
    for i in range(1, len(strs)+1):
        
        num_zeros = strs[i-1].count('0')
        num_ones = strs[i-1].count('1')

        for j in range(m+1):
            
            for k in range(n+1):
                if j >= num_zeros and k >= num_ones:
                    dp[i][j][k] = max(dp[i-1][j][k], 1 + dp[i-1][j-num_zeros][k-num_ones])
                else:
                    dp[i][j][k] = dp[i-1][j][k]
    
    ans = dp[len(strs)][m][n]
    
    return ans