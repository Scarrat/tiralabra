from heapq import heappush, heappop, heapify
from collections import defaultdict
import re
from bitarray import bitarray



class Huffman:

    def __init__(self):
        self.huff_dict = None

    def read_noncoded(self, file):
        with open(file, "r") as file:
            text = file.read()

        return text

    def read_encoded(self, file):
        decoded = bitarray()


        data = open(file, 'rb').read()
        info = data.split(b'\n')
        huffdict = str(info[0])
        huffdict = huffdict[2:len(huffdict)-1]
        bitpad = str(info[1])
        bitpad = bitpad[2:len(bitpad)-1]
        # decoded.frombytes(info[2])

        rdata = info[2:]
        text = b''.join(rdata)
        decoded.frombytes(text)



        print(huffdict)
        # print(bitpad)
        # print(decoded)


        

        return huffdict, bitpad, decoded

    def encode_data(self, text):

        # pad = (8 - len(text)) % 8
        

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

        pad = 8 - (len(encoded_data) % 8)
        


        with open("files/encoded.txt", "w") as file:
            file.write(str(self.huff_dict))
            
        with open("files/encoded.txt", "a") as file:
            file.write("\n")

        with open("files/encoded.txt", "a") as file:
            file.write(str(pad))

        with open("files/encoded.txt", "a") as file:
            file.write("\n")

        with open("files/encoded.txt", "ab") as file:
            file.write(encoded_data)

         
            

    def decode_data(self, decoded):
        dictionary, pad, text = decoded
        newdic = dict()


        dictionary = dictionary.split(", ")
        for d in dictionary:
            vals = re.findall(r"'([^']*)'", d)
            newdic[vals[0]] = bitarray(vals[1])
        if int(pad) != 8:
            text = text[:-int(pad)]
        
        if '\\\\n' in newdic:
            newdic['\n'] = newdic.pop('\\\\n')
        if '\\xe2\\x80\\xa6' in newdic:
            newdic['...'] = newdic.pop('\\xe2\\x80\\xa6')
        if '\\xe2\\x80\\x99' in newdic:
            newdic["'"] = newdic.pop('\\xe2\\x80\\x99')

        
        print(newdic)
        text = text.decode(newdic)
        text = ''.join(text)
        # text = text.replace('\\n', '\n')
        # text = text.replace("\\xe2\\x80\\x99", "'")


        with open("files/decoded.txt", "w") as file:
            file.write(text)


        # texti = open("files/decoded.txt","r").read().replace('\\n','\n')

        # with open("files/decoded.txt", "w") as file:
        #     file.write(texti)



