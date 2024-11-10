import heapq
from collections import Counter


def Probabilities(message):
    # Convert message to uppercase and remove spaces
    message = message.upper().replace(' ', '')
    # Calculate frequency of each character
    freq = Counter(message)
    # Calculate probability for each character
    P = [freq[char] / len(message) for char in sorted(freq)]
    return P, freq


def build_heap(freq):
    # Create a heap with normalized weights and empty codes
    heap = [[weight / sum(freq.values()), [char, '']] for char, weight in sorted(freq.items())]
    heapq.heapify(heap)
    return heap


def build_tree(heap):
    # Build Huffman Tree
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        for pair in left[1:]:
            pair[1] = '0' + pair[1]
        for pair in right[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [left[0] + right[0]] + left[1:] + right[1:])
    return heap[0]


# Message and function calls
message = 'aaabbbbbccccccddddee'
P, freq = Probabilities(message)
print('Probabilities: ', P)  # Print probabilities

heap = build_heap(freq)
tree = build_tree(heap)
print('Tree:', tree)  # Print tree

# Print character encoding
for pair in tree[1:]:
    print(pair[0], '->', pair[1])
