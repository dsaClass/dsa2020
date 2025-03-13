import heapq
from collections import defaultdict, deque

class Node:
    def __init__(self, chars, freq, left=None, right=None):
        self.chars = chars
        self.freq = freq
        self.left = left
        self.right = right
    
    def __lt__(self, other):
        if self.freq == other.freq:
            return min(self.chars) < min(other.chars)
        return self.freq < other.freq

def build_huffman_tree(char_freq):
    heap = []
    for char, freq in char_freq.items():
        heapq.heappush(heap, Node({char}, freq))
    
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged_chars = left.chars.union(right.chars)
        merged_freq = left.freq + right.freq
        heapq.heappush(heap, Node(merged_chars, merged_freq, left, right))
    
    return heapq.heappop(heap)

def generate_codes(root, code, codes):
    if root is None:
        return
    if not root.left and not root.right:
        codes[list(root.chars)[0]] = code
        return
    generate_codes(root.left, code + '0', codes)
    generate_codes(root.right, code + '1', codes)

def encode_string(s, codes):
    encoded = ''
    for char in s:
        encoded += codes[char]
    return encoded

def decode_string(encoded, root):
    decoded = ''
    current = root
    for bit in encoded:
        if bit == '0':
            current = current.left
        else:
            current = current.right
        if not current.left and not current.right:
            decoded += list(current.chars)[0]
            current = root
    return decoded

def main():
    n = int(input())
    char_freq = {}
    for _ in range(n):
        char, freq = input().split()
        char_freq[char] = int(freq)
    
    root = build_huffman_tree(char_freq)
    codes = {}
    generate_codes(root, '', codes)
    
    while True:
        try:
            line = input().strip()
            if not line:
                continue
            if line[0] in {'0', '1'}:
                print(decode_string(line, root))
            else:
                print(encode_string(line, codes))
        except EOFError:
            break

if __name__ == "__main__":
    main()