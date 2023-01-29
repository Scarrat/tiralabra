from heapq import heappush, heappop, heapify
from collections import defaultdict
from bitarray import bitarray


class Huffman:

    def __init__(self):
        self.bitpad = 0
        self.huff_dict = None

    def read_noncoded(self, file):
        with open(file, "r") as file:
            text = file.read()

        return text

    def read_encoded(self, file):
        decoded = bitarray()

        with open(file, "rb") as r:
            decoded.fromfile(r)

        return decoded

    def encode_data(self, text):

        # creates frequency library
        freq_dict = defaultdict(int)
        for char in text:
            freq_dict[char] += 1

        # creates huffman tree
        heap = [[frequency, [char, ""]]
                for char, frequency in freq_dict.items()]
        heapify(heap)
        while len(heap) > 1:
            right = heappop(heap)
            left = heappop(heap)
            for pair in right[1:]:
                pair[1] = '0' + pair[1]
            for pair in left[1:]:
                pair[1] = '1' + pair[1]
            heappush(heap, [right[0] + left[0]] + right[1:] + left[1:])

        # creates the encoding dictionary
        huff_list = right[1:] + left[1:]
        self.huff_dict = {a[0]: bitarray(str(a[1])) for a in huff_list}

        # encodes the data
        encoded_data = bitarray()
        encoded_data.encode(self.huff_dict, text)

        # adds extra bits for bytes to work correctly
        self.bitpad = 8 - (len(encoded_data) % 8)

        with open("files/encoded.bin", "wb") as file:
            file.write(encoded_data)

    def decode_data(self, decoded):

        decoded = decoded[:-self.bitpad]

        decoded = decoded.decode(self.huff_dict)
        decoded = ''.join(decoded)

        with open("files/decoded.txt", "w") as file:
            file.write(decoded)
