def find_max_form(strs, m, n):
    dp_lst = []

    for _ in range(len(strs)+1):

        row = []
        for _ in range(m+1):
            elements = [0] * (n+1)
            row.append(elements)

        dp_lst.append(row)

    for i in range(1,len(strs)+1):

        count_zeros = strs[i-1].count('0')
        count_ones = strs[i-1].count('1')

        for j in range(m+1):
                
            for k in range(n+1):
                previous_max = dp_lst[i-1][j][k]
                if j >= count_zeros and k >= count_ones:
                    
                    current_max = 1 + dp_lst[i-1][j-count_zeros][k-count_ones]
                    dp_lst[i][j][k] = max(previous_max, current_max)
                else:
                    dp_lst[i][j][k] = previous_max

    ans = dp_lst[len(strs)][m][n]

    return ans