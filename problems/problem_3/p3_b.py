def  local_search_2opt(cost_matrix, candidate):
    candidate = list(candidate)
    def compute_cost(cost_matrix, sequence):
        sum = 0
        for i in range(len(sequence) - 1):
            sum += cost_matrix[sequence[i] - 1][sequence[i+1] - 1]
        return sum

    
    last_candidate = candidate
    
    while candidate == last_candidate: 
        
        last_candidate = candidate
        
        for i in range(1,len(candidate)-1):
            # Create new candidiate
            new_candidate_front = candidate.copy()
            new_candidate_back = candidate.copy()
            new_candidate_front[i-1], new_candidate_front[i] = new_candidate_front[i], new_candidate_front[i-1]
            new_candidate_back[i+1], new_candidate_back[i] = new_candidate_back[i], new_candidate_front[i+1]
    
            # Compute cost of both candidates
            candidate_cost = compute_cost(cost_matrix, candidate)
            new_candidate_front_cost = compute_cost(cost_matrix, new_candidate_front)
            new_candidate_back_cost = compute_cost(cost_matrix, new_candidate_back)
    
            # set up cost dictionary
            cost_dict = {}
            cost_dict[candidate_cost] = candidate
            cost_dict[new_candidate_front_cost] = new_candidate_front
            cost_dict[new_candidate_back_cost] = new_candidate_back
    
            # get min cost from dict
            min_key = min(cost_dict)
            candidate = cost_dict[min_key]
            
        
    return tuple(candidate)
            
            
    
if __name__ == "__main__":
    cost_matrix = [
      [float('inf'), 3, 5],
      [3, float('inf'), 7],
      [5, 7, float('inf')]]
    ans = local_search_2opt(cost_matrix, (2, 3, 1)),

    print(ans)

      