import unittest
from lz77 import Lz77
import os

class TestLz77(unittest.TestCase):
    def setUp(self):
        self.lz77 = Lz77()

    def test_read_noncoded(self):
        self.assertEqual(self.lz77.read_noncoded("inputs/test.txt"),b"Hello hello")

    def test_encoding(self):
        self.lz77.compress(self.lz77.read_noncoded("inputs/test.txt"))
        self.lz77.decompress(self.lz77.read_encoded("outputs/compressedlz.txt"))
        self.assertEqual(self.lz77.read_noncoded("outputs/decompressedlz.txt"),self.lz77.read_noncoded("inputs/test.txt"))
        os.remove("outputs/compressedlz.txt")
        os.remove("outputs/decompressedlz.txt")

    def test_compression(self):
        self.lz77.compress(self.lz77.read_noncoded("inputs/input.txt"))
        orig = os.path.getsize("inputs/input.txt")
        compr = os.path.getsize("outputs/compressedlz.txt")
        print(compr,orig)
        self.assertTrue(compr/orig < 0.6)
        os.remove("outputs/compressedlz.txt")
