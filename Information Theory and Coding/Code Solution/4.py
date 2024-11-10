def calcRedundantBits(m):
    for i in range(m):
        if(2**i >= m + i + 1):
            return i

def posRedundantBits(data, r):
    j = 0  # Redundant bit count
    k = 1  # Data bit count
    m = len(data)
    res = ''
    
    for i in range(1, m + r + 1):
        if i == 2**j:
            res = res + '0'  # Insert '0' at positions of power of 2 (redundant bits)
            j += 1
        else:
            res = res + data[-1 * k]  # Insert actual data bits
            k += 1

    return res[::-1]  # Reverse to match actual order

def calcParityBits(arr, r):
    n = len(arr)
    for i in range(r):
        val = 0
        for j in range(1, n + 1):
            if j & (2**i) == (2**i):
                val = val ^ int(arr[-1 * j])  # Check bits for parity
        arr = arr[:n - (2**i)] + str(val) + arr[n - (2**i) + 1:]  # Set the parity bit
    return arr

def detectError(arr, r):
    n = len(arr)
    res = 0
    for i in range(r):
        val = 0
        for j in range(1, n + 1):
            if j & (2**i) == (2**i):
                val = val ^ int(arr[-1 * j])
        res = res + val * (10**i)
    return int(str(res), 2)

# User input
data = input("Enter the binary data to encode (e.g., '01101'): ")

# Validate binary input
if not all(bit in '01' for bit in data):
    print("Invalid input. Please enter a binary number (0s and 1s).")
else:
    # Encode the data
    m = len(data)
    r = calcRedundantBits(m)
    encoded_data = posRedundantBits(data, r)
    encoded_data = calcParityBits(encoded_data, r)
    print("Generated Hamming Code:", encoded_data)

    # Simulate receiving the data and detecting errors
    received_data = input("Enter the received Hamming code 001101110: ")
    if len(received_data) != len(encoded_data):
        print("Received data length does not match encoded data length.")
    else:
        error_pos = detectError(received_data, r)
        if error_pos == 0:
            print("No error detected in the received message.")
        else:
            print(f"Error detected at position from the right side: {error_pos}")
            
