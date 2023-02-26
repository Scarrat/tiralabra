import unittest
from lz77 import Lz77
import os

class TestLz77(unittest.TestCase):
    def setUp(self):
        self.lz77 = Lz77()

    def test_read_noncoded(self):
        self.assertEqual(self.lz77.read_noncoded("files/test.txt"),b"Hello")

    def test_encoding(self):
        self.lz77.compress(self.lz77.read_noncoded("files/test.txt"))
        self.lz77.decompress(self.lz77.read_encoded("files/compressedlz.txt"))
        self.assertEqual(self.lz77.read_noncoded("files/decompressedlz.txt"),self.lz77.read_noncoded("files/test.txt"))
        os.remove("files/compressedlz.txt")
        os.remove("files/decompressedlz.txt")

    def test_compression(self):
        self.lz77.compress(self.lz77.read_noncoded("files/input.txt"))
        orig = os.path.getsize("files/input.txt")
        compr = os.path.getsize("files/compressedlz.txt")
        print(compr,orig)
        self.assertTrue(compr/orig < 0.6)
        os.remove("files/compressedlz.txt")
