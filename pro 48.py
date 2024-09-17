import heapq
from collections import defaultdict, namedtuple
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
def generate_huffman_codes(node, prefix='', codebook={}):
    if node is not None:
        if node.char is not None:
            codebook[node.char] = prefix
        generate_huffman_codes(node.left, prefix + '0', codebook)
        generate_huffman_codes(node.right, prefix + '1', codebook)
    return codebook
n = 4
characters = ['a', 'b', 'c', 'd']
frequencies = [5, 9, 12, 13]
encoded_string = '1101100111110'
huffman_tree = build_huffman_tree(characters, frequencies)
huffman_codes = generate_huffman_codes(huffman_tree)
def decode_huffman(encoded_string, huffman_tree):
    decoded_message = []
    current_node = huffman_tree
    for bit in encoded_string:
        current_node = current_node.left if bit == '0' else current_node.right
        if current_node.char is not None:
            decoded_message.append(current_node.char)
            current_node = huffman_tree
    return ''.join(decoded_message)
output = decode_huffman(encoded_string, huffman_tree)
print(output) 
