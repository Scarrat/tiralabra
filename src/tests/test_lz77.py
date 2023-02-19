import unittest
from lz77 import Lz77
import os

class TestLz77(unittest.TestCase):
    def setUp(self):
        self.lz77 = Lz77()

    def test_read_noncoded(self):
        self.assertEqual(self.lz77.read_noncoded("files/test.txt"),"Hello")
