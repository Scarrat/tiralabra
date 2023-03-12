import cProfile
from huffman import Huffman
from lz77 import Lz77
import time

huff = Huffman()
lz = Lz77()
testcode1 = """
data = huff.read_noncoded("inputs/100.txt")
huff.encode_data(data)"""
testcode2 = """
data2 = lz.read_noncoded("inputs/100.txt")
lz.compress(data2)"""

def testhuff(file):
    t0 = time.time()
    data = huff.read_noncoded(file)
    huff.encode_data(data)
    t1 = time.time()
    total = t1-t0
    print(file," huffman ", round(total, 4))

def testlz(file):
    t0 = time.time()
    data = lz.read_noncoded(file)
    lz.compress(data)
    t1 = time.time()
    total = t1-t0
    print(file," lz ", round(total, 4))



if __name__ == "__main__":
    cProfile.run(testcode1)
    cProfile.run(testcode2)
    testhuff("inputs/5.txt")
    testhuff("inputs/10.txt")
    testhuff("inputs/50.txt")
    testhuff("inputs/100.txt")
    testhuff("inputs/nonsense.txt")
    testhuff("inputs/rj.txt")
    testhuff("inputs/moby.txt")
    print("")
    testlz("inputs/5.txt")
    testlz("inputs/10.txt")
    testlz("inputs/50.txt")
    testlz("inputs/100.txt")
    testlz("inputs/nonsense.txt")
    testlz("inputs/rj.txt")
    testlz("inputs/moby.txt")