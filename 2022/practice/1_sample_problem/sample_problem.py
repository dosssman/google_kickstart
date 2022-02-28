import numpy as np

# Read the number of cases from input
n_cases = int(input("Number of cases?: "))

for case_i in range(n_cases):
    # Read N: # of bags; M: # of kids
    N_M = input("Number of bags ? Kids ?: ")
    N, M = N_M.split(' ')
    N, M = int(N), int(M)
    
    # Read C_i: number of candies per bag
    c_i_list = input("Number of candies per bags? : ")
    c_i_list = c_i_list.split(' ')
    
    # Total # of candies
    n_candies = int(np.sum([int(c_i) for c_i in c_i_list]))
    
    # Remainder after distribution
    remaining_candies = n_candies % M
    
    print(f"Case #{case_i+1}: {remaining_candies}")
