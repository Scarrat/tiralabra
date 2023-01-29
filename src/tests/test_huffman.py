import unittest
from huffman import Huffman
import os

class TestHuffman(unittest.TestCase):
    def setUp(self):
        self.huffman = Huffman()

    def test_read_noncoded(self):
        self.assertEqual(self.huffman.read_noncoded("files/test.txt"),"Hello")

    def test_encoding(self):
        self.huffman.encode_data(self.huffman.read_noncoded("files/test.txt"))
        self.huffman.decode_data(self.huffman.read_encoded("files/encoded.bin"))
        self.assertEqual(self.huffman.read_noncoded("files/decoded.txt"),"Hello")
        os.remove("files/encoded.bin")
        os.remove("files/decoded.txt")

    # python3 -m unittest ./tests/test_huffman.py