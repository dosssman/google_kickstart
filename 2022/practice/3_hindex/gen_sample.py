import random

MAX_T = 2
MAX_C = int(1e5)
MAX_N = 6 # int(1e3)

with open("sample_gen.txt", "a") as f:
    f.write(f"{MAX_T}\n")
    for _ in range(MAX_T):
        N = random.randint(1, MAX_N)
        f.write(f"{N}\n")
        f.write(' '.join([str(random.randint(1, MAX_C)) for _ in range(N)]))
        f.write("\n")
    
    f.write("\n")