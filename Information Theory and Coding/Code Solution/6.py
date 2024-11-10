import math
import heapq
from collections import defaultdict

# Step 1: Calculate the frequency of each symbol
def calculate_frequency(message):
    frequency = defaultdict(int)
    for char in message:
        frequency[char] += 1
    return frequency

# Step 2: Calculate the entropy of the message
def calculate_entropy(frequencies, total_symbols):
    entropy = 0
    for freq in frequencies.values():
        p = freq / total_symbols
        entropy += p * math.log2(p)
    return -entropy

# Step 3: Build the Huffman tree
def build_huffman_tree(frequencies):
    heap = [[weight, [symbol, ""]] for symbol, weight in frequencies.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])

    return sorted(heap[0][1:], key=lambda p: (len(p[-1]), p))

# Step 4: Calculate the expected code length from the Huffman code
def calculate_expected_length(huffman_codes, frequencies, total_symbols):
    expected_length = 0
    for symbol, code in huffman_codes:
        probability = frequencies[symbol] / total_symbols
        expected_length += probability * len(code)
    return expected_length

# Step 5: Main function to execute the process
def main(message):
    # Calculate the frequencies of symbols
    frequencies = calculate_frequency(message)
    total_symbols = len(message)

    # Calculate the entropy of the message
    entropy = calculate_entropy(frequencies, total_symbols)

    # Build the Huffman tree and get the Huffman codes
    huffman_codes = build_huffman_tree(frequencies)

    # Calculate the expected code length using Huffman coding
    expected_length = calculate_expected_length(huffman_codes, frequencies, total_symbols)

    # Output results
    print(f"Message: {message}")
    print(f"Frequencies: {frequencies}")
    print(f"Entropy: {entropy:.4f} bits")
    print(f"Huffman Codes: {huffman_codes}")
    print(f"Expected Code Length: {expected_length:.4f} bits")
    print(f"Optimality Check: {'Optimal' if abs(entropy - expected_length) < 0.01 else 'Not Optimal'}")

# Example usage
message = "bccabbddaeccbbaeddcc"
main(message)
