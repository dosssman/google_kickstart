import numpy as np
from collections import OrderedDict

T = int(input())

for t in range(T):
    # Read N: number of papers written in this case
    N = int(input())

    # Read list of C_i: # of citation per paper
    paper_citation_list = [int(i) for i in input().split(' ')]

    h_dict = OrderedDict()
    h_dict[1] = 0

    h = 1 # Minimal num citation guaranteed
    h_ubound = 1
    post_pub_h_list = []

    for c in paper_citation_list:
        c_v = 1

        for k, v in h_dict.items():
            h_ubound_found = False
            if k <= c:
                h_dict[k] += 1
            else:
                c_v += 1 if c in h_dict.items() else v
            
            if not h_ubound_found and k > h:
                # if v >= h:
                h_ubound = k
                h_ubound_found = True
            
        if c not in h_dict.keys():
            h_dict[c] = c_v
            if c_v > h:
                h_ubound = c
        
        ## Attempot at more efficient
        print(np.where(np.greater(list(h_dict.keys()), h)))

        k_list = sorted(list(h_dict.keys()))
        h_idx_ubnd_idx = 0
        for idx, is_greater in enumerate(np.greater(k_list, h)):
            if is_greater:
                h_idx_ubnd_idx = idx
                break
        # print("\tk_list: ", k_list)
        # print("\tbnd idx in k_list: ", idx)
        h_index_ubnd = k_list[h_idx_ubnd_idx]
        h_ubnd_v = h_dict[h_index_ubnd]
        for j in range(h+1, h_index_ubnd+1):
            # print(f"\tIterate of over the j= {j}")
            if j == h_ubnd_v:
                h = j
                break

        post_pub_h_list.append(str(h))

        # print(f"Read {c_i} as the {i+1}-th paper cit. count")
    #     print("{ ", end="")
    #     for k, v in h_dict.items():
    #         print(f"{k}: {v}, ", end="")
    #     print("}; " f"h_ubnd: {h_ubound}")
    # print()
    # print(post_pub_h_list)
    print(f"Case #{t+1}: {' '.join(post_pub_h_list)}")