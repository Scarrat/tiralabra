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
        self.huffman.decode_data(self.huffman.read_encoded("files/compressedhuff.txt"))
        self.assertEqual(self.huffman.read_noncoded("files/decompressedhuff.txt"),self.huffman.read_noncoded("files/test.txt"))
        os.remove("files/compressedhuff.txt")
        os.remove("files/decompressedhuff.txt")

    def test_compression(self):
        self.huffman.encode_data(self.huffman.read_noncoded("files/input.txt"))
        orig = os.path.getsize("files/input.txt")
        compr = os.path.getsize("files/compressedhuff.txt")
        print(compr,orig)
        self.assertTrue(compr/orig < 0.6)
        os.remove("files/compressedhuff.txt")

    # python3 -m unittest ./tests/test_huffman.py