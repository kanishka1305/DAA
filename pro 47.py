import heapq
from collections import defaultdict
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    def __lt__(self, other):
        return self.freq < other.freq
def build_huffman_tree(characters, frequencies):
    heap = [Node(char, freq) for char, freq in zip(characters, frequencies)]
    heapq.heapify(heap)
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)
    return heap[0]
def generate_codes(node, prefix="", codebook={}):
    if node is not None:
        if node.char is not None:
            codebook[node.char] = prefix
        generate_codes(node.left, prefix + "0", codebook)
        generate_codes(node.right, prefix + "1", codebook)
    return codebook
def huffman_codes(characters, frequencies):
    root = build_huffman_tree(characters, frequencies)
    codes = generate_codes(root)
    return [(char, codes[char]) for char in characters]
n = 4
characters = ['a', 'b', 'c', 'd']
frequencies = [5, 9, 12, 13]
output = huffman_codes(characters, frequencies)
print(output)
