

class Lz77:

    def read_noncoded(self, file):
        """Reads data from a non-compressed file and returns the data"""
        with open(file, "r") as file:
            text = file.read()

        return text

    def encode_data(self, text):
        """Encodes the given text data and writes it into a file"""