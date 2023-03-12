from heapq import heappush, heappop, heapify
from collections import defaultdict
from bitarray import bitarray


class Huffman:
    """class for compressing and decompressing files with huffman algorithm"""

    def __init__(self):
        self.huff_dict = None

    def read_noncoded(self, file):
        """Reads data from a non-compressed file and returns the data"""
        with open(file, "r") as f:
            text = f.read()

        return text

    def read_encoded(self, file):
        """Reads data from a compressed file, splits it into the dictionary,
         padding and text, and returns all of them"""
        decoded = bitarray()

        with open(file, "rb") as f:
            readdict = f.readline().decode('utf-8')
            huffdict = eval(readdict)
            bitpad = f.readline().decode('utf-8')
            text = f.read()
            decoded.frombytes(text)

        return huffdict, bitpad, decoded

    def encode_data(self, text):
        """Encodes the given text data and writes it into a file"""

        # create frequency library
        freq_dict = defaultdict(int)
        for sym in text:
            freq_dict[sym] += 1

        # create huffman tree
        heap = [[frequency, [sym, ""]]
                for sym, frequency in freq_dict.items()]
        heapify(heap)
        while len(heap) > 1:
            # pop the node with the smallest frequency from the heap
            right = heappop(heap)
            # pop the node with the second smallest frequency from the heap
            left = heappop(heap)
            for pair in right[1:]:
                # add a 0 to the code of each symbol in the right node
                pair[1] = '0' + pair[1]
            for pair in left[1:]:
                # add a 1 to the code of each symbol in the left node
                pair[1] = '1' + pair[1]
            # push the merged node back into the heap
            heappush(heap, [right[0] + left[0]] + right[1:] + left[1:])

        # create the encoding dictionary
        # create a list of symbol and code pairs
        huff_list = right[1:] + left[1:]
        # create a dictionary from the list of symbol and code pairs
        self.huff_dict = {pair[0]: bitarray(
            str(pair[1])) for pair in huff_list}

        # encode the data
        encoded_data = bitarray()
        encoded_data.encode(self.huff_dict, text)

        # make note of the extra bits needed for decoding
        pad = 8 - (len(encoded_data) % 8)

        # write the data into a file as bytes
        with open("outputs/compressedhuff.txt", "wb") as file:
            file.write(self.huff_dict.__repr__().encode("utf-8"))
            file.write(b"\n")
            file.write(str(pad).encode("utf-8"))
            file.write(b"\n")
            file.write(encoded_data)

    def decode_data(self, decoded):
        """decodes given data and writes it into an output file"""
        dictionary, pad, text = decoded

        # remove extra bits added during encoding
        if int(pad) != 8:
            text = text[:-int(pad)]

        text = text.decode(dictionary)
        text = ''.join(text)
        # write the decompressed text into a file
        with open("outputs/decompressedhuff.txt", "w") as file:
            file.write(text)
