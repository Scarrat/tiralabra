
from ui import UI

if __name__ == "__main__":
    ui = UI()
    ui.start()


    # huff = Huffman()
    # lz = Lz77()
    # while True:
            
    #     compress_method = input("Enter 1 for Huffman and 2 for Lempel-Ziv, empty to exit ")
    #     if compress_method == "":
    #         break

    #     selection = input("Enter 1 for compression and 2 for decompression: ")
    #     if selection == "1":
    #         file_path = input("Name of the file: ")

    #     if compress_method == "1" and selection == "1":
    #         data = huff.read_noncoded(f"files/{file_path}")
    #         huff.encode_data(data)
    #         size1 = os.path.getsize(f"files/{file_path}")
    #         size2 = os.path.getsize(f"files/compressedhuff.txt")
    #         print("File compressed at files/compressedhuff.txt")
    #         diff = (size2 / size1) * 100
    #         print(f"File size is {round(diff)}% of the original size")
        
    #     if compress_method == "1" and selection == "2":
    #         data = huff.read_encoded("files/compressedhuff.txt")
    #         huff.decode_data(data)
            
    #         print("File decompressed at files/decompressedhuff.txt")

    #     if compress_method == "2" and selection == "1":
    #         t0 = time.time()
    #         data = lz.read_noncoded(f"files/{file_path}")
    #         lz.compress(data)
    #         size1 = os.path.getsize(f"files/{file_path}")
    #         size2 = os.path.getsize(f"files/compressedlz.txt")
    #         print("File compressed at files/compressedlz.txt")
    #         diff =(size2 / size1) * 100
    #         print(f"File size is {round(diff)}% of the original size")

    #     if compress_method == "2" and selection == "2":
    #         t0 = time.time()
    #         data = lz.read_encoded("files/compressedlz.txt")
    #         lz.decompress(data)
    #         print("File decompressed at files/decompressedlz.txt")
    #     print("")


# data = compressorhuffman.read_noncoded("files/input.txt")

# compressorhuffman.encode_data(data)

# data = compressorhuffman.read_encoded("files/encoded.txt")
# compressorhuffman.decode_data(data)


# t0 = time.time()
# data = compressorlz77.read_noncoded("files/darth.txt")
# compressorlz77.compress(data)
# data = compressorlz77.read_encoded("files/compressed.txt")
# compressorlz77.decompress(data)

# t1 = time.time()
# total = t1-t0
# print(total)



    

