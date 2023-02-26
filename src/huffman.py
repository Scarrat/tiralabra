from heapq import heappush, heappop, heapify
from collections import defaultdict
from bitarray import bitarray


class Huffman:

    def __init__(self):
        self.huff_dict = None

    def read_noncoded(self, file):
        """Reads data from a non-compressed file and returns the data"""
        with open(file, "r") as file:
            text = file.read()

        return text

    def read_encoded(self, file):
        """Reads data from a compressed file, splits it into 3 and returns all of them"""
        decoded = bitarray()

        with open(file, "rb") as r:
            readdict = r.readline().decode('utf-8')
            huffdict = eval(readdict)
            bitpad = r.readline().decode('utf-8')
            text = r.read()
            decoded.frombytes(text)

        return huffdict, bitpad, decoded

    def encode_data(self, text):
        """Encodes the given text data and writes it into a file"""

        # creates frequency library
        freq_dict = defaultdict(int)
        for sym in text:
            freq_dict[sym] += 1

        # creates huffman tree
        heap = [[frequency, [sym, ""]]
                for sym, frequency in freq_dict.items()]
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

        # makes note of the extra bits needed for decoding
        pad = 8 - (len(encoded_data) % 8)

        with open("files/compressedhuff.txt", "wb") as file:
            file.write(self.huff_dict.__repr__().encode("utf-8"))
            file.write(b"\n")
            file.write(str(pad).encode("utf-8"))
            file.write(b"\n")
            file.write(encoded_data)

    def decode_data(self, decoded):
        """decodes given data and writes it into an output file"""
        dictionary, pad, text = decoded

        if int(pad) != 8:
            text = text[:-int(pad)]

        text = text.decode(dictionary)
        text = ''.join(text)

        with open("files/decompressedhuff.txt", "w") as file:
            file.write(text)
