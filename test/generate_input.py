import random
import string

alphabet = list("abcdefghij")
num_files = 10

for t in range(1, num_files + 1):
    k = len(alphabet)
    values = {c: random.randint(1, 10) for c in alphabet}
    
    n = random.randint(25, 50)
    m = random.randint(25, 50)
    A = ''.join(random.choice(alphabet) for _ in range(n))
    B = ''.join(random.choice(alphabet) for _ in range(m))
    
    filename = f"input/input{t}.in"
    with open(filename, "w") as f:
        f.write(f"{k}\n")
        for c in alphabet:
            f.write(f"{c} {values[c]}\n")
        f.write(f"{A}\n")
        f.write(f"{B}\n")
    print(f"Created {filename} (lengths {n}, {m})")