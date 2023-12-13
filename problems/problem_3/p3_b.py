def  local_search_2opt(cost_matrix, candidate):
    candidate = list(candidate)
    def compute_cost(cost_matrix, sequence):
        sum = 0
        for i in range(len(sequence) - 1):
            sum += cost_matrix[sequence[i] - 1][sequence[i+1] - 1]
        return sum

    
    old_cost = None

    while old_cost != compute_cost(cost_matrix, candidate):
        old_cost = compute_cost(cost_matrix, candidate)
        cost_dict = {str(candidate): old_cost}
        # print(cost_dict)
        n = len(candidate)
        for i in range(n):
            for j in range(i+1, n):
                new_candidate = candidate.copy()
                new_candidate[i], new_candidate[j] = new_candidate[j], new_candidate[i]

                # add to cost dictionary
                cost_dict[str(new_candidate)] = compute_cost(cost_matrix, new_candidate)
        
        # get min cost from dict
        min_key = min(cost_dict, key=cost_dict.get)
        str_list = min_key.strip('[]')
        actual_list = [int(i) for i in str_list.split(',')]
        candidate = actual_list
            
        
    return tuple(candidate)
            
            
    
# if __name__ == "__main__":
#     cost_matrix = [
#       [float('inf'), 3, 5],
#       [3, float('inf'), 7],
#       [5, 7, float('inf')]]
#     ans = local_search_2opt(cost_matrix, (2, 3, 1)),

#     print(ans)

      