import time
from lz77 import Lz77
from huffman import Huffman


compressorlz77 = Lz77()
compressorhuffman = Huffman()






data = compressorhuffman.read_noncoded("files/input.txt")

compressorhuffman.encode_data(data)

data = compressorhuffman.read_encoded("files/encoded.txt")
compressorhuffman.decode_data(data)


# t0 = time.time()
# compressorlz77.compress("files/input.txt")
# compressorlz77.decompress(cinput_file, coutput_file)

# t1 = time.time()
# total = t1-t0
# print(total)



    

