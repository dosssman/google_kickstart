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

        for j in range(h+1, h_ubound+1):
            if h_dict[h_ubound] <= h:
                # print("\tMax j: ", j)
                break
                
            if j in h_dict.keys() and h_dict[j] >= j:
                h = j
                # print("\tMax j: ", j)
                break
            
            if h_dict[h_ubound] >= j:
                h = j
                # print("\tMax j: ", j)
                break
        # h = max(h, min(h_ubound, h_dict[h_ubound]))

        post_pub_h_list.append(str(h))

        # print(f"Read {c_i} as the {i+1}-th paper cit. count")
    #     print("{ ", end="")
    #     for k, v in h_dict.items():
    #         print(f"{k}: {v}, ", end="")
    #     print("}; " f"h_ubnd: {h_ubound}")
    # print()
    # print(post_pub_h_list)
    print(f"Case #{t+1}: {' '.join(post_pub_h_list)}")