import numpy as np

def encode(msg, K, n):
    g, v = [], []
    
    # Collect generator polynomials
    for i in range(n):
        sub_g = list(map(int, input(f'Enter bits for generator {i}: ').split()))
        if len(sub_g) != K:
            raise ValueError(f'You entered {len(sub_g)} bits.\n need to enter {K} bits')
        g.append(sub_g)
    
    # Encoding each generator polynomial with the message
    for i in range(n):
        res = list(np.poly1d(g[i]) * np.poly1d(msg))
        v.append(res)
    
    # Find maximum length for padding
    listMax = max(len(l) for l in v)
    for i in range(n):
        if len(v[i]) != listMax:
            tmp = [0] * (listMax - len(v[i]))
            v[i] = tmp + v[i]
    
    # Construct the final encoded message
    res = []
    for i in range(listMax):
        res += [v[j][i] % 2 for j in range(n)]
    
    # Convert np.int64 to standard Python integers
    res = [int(x) for x in res]
    return res

# Input message and parameters
message = list(map(int, input('Enter message: ').split()))
K = int(input('Constraints: '))
n = int(input('Number of output(generator): '))

# Display the encoded message
print('Encoded Message:', encode(message, K, n))
