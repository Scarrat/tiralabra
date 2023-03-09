import unittest
from huffman import Huffman
import os

class TestHuffman(unittest.TestCase):
    def setUp(self):
        self.huffman = Huffman()

    def test_read_noncoded(self):
        self.assertEqual(self.huffman.read_noncoded("inputs/test.txt"),"Hello")

    def test_encoding(self):
        self.huffman.encode_data(self.huffman.read_noncoded("inputs/test.txt"))
        self.huffman.decode_data(self.huffman.read_encoded("outputs/compressedhuff.txt"))
        self.assertEqual(self.huffman.read_noncoded("outputs/decompressedhuff.txt"),self.huffman.read_noncoded("inputs/test.txt"))
        os.remove("outputs/compressedhuff.txt")
        os.remove("outputs/decompressedhuff.txt")

    def test_compression(self):
        self.huffman.encode_data(self.huffman.read_noncoded("inputs/input.txt"))
        orig = os.path.getsize("inputs/input.txt")
        compr = os.path.getsize("outputs/compressedhuff.txt")
        print(compr,orig)
        self.assertTrue(compr/orig < 0.6)
        os.remove("outputs/compressedhuff.txt")

    # python3 -m unittest ./tests/test_huffman.py