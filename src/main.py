from huffman import Huffman


if __name__ == "__main__":
    encoder = Huffman()
    
    data_b = encoder.read_noncoded("files/test.txt")
    encoder.encode_data(data_b)

    data_a = encoder.read_encoded("files/encoded.txt")
    encoder.decode_data(data_a)


    

