import tkinter as tk
from huffman import Huffman
from lz77 import Lz77
import os


class UI:

    def __init__(self):
        self.huffman = Huffman()
        self.lz77 = Lz77()
        self.lbl_info = None
    def start(self):
        window = tk.Tk()
        window.title("Compressor")
        window.resizable(width=False, height=False)


        #create the frame and text of the GUI
        frm_entry = tk.Frame(master=window)
        ent_file = tk.Entry(master=window, width=20)
        lbl_huff = tk.Label(master=window, text="Huffman:")
        lbl_lz = tk.Label(master=window, text="Lempel-Ziv:")
        self.lbl_info = tk.Label(master=window, text="")

        ent_file.grid(row=0, column=1, sticky="e")
        lbl_huff.grid(row=1, column=0, sticky="w")
        lbl_lz.grid(row=1, column = 2)
        btn_huff_compress = tk.Button(
            master=window,
            text="compress",
            command=lambda: self.lbl_info.config(text = self.huff_compress(ent_file.get()))

        )
        # create the buttons for the GUI
        btn_huff_decompress = tk.Button(
            master=window,
            text="decompress",
            command=lambda: [self.huff_decompress(ent_file.get()), self.lbl_info.config(text= "done decompressing huff")]

        )
        btn_lz_compress = tk.Button(
            master=window,
            text="compress",
            command=lambda: self.lbl_info.config(text = self.lz_compress(ent_file.get()))

        )
        btn_lz_decompress = tk.Button(
            master=window,
            text="decompress",
            command=lambda: [self.lz_decompress(ent_file.get()), self.lbl_info.config(text= "done decompressing lz")]

        )
        # position everything
        frm_entry.grid(row=0, column=0, padx=10)
        btn_huff_compress.grid(row=2, column=0, sticky="w")
        btn_huff_decompress.grid(row=3, column=0, sticky="w")
        btn_lz_compress.grid(row=2, column=2, sticky="e")
        btn_lz_decompress.grid(row=3, column=2,sticky="e")
        self.lbl_info.grid(row=4,column=1)


        window.mainloop()

    # all the main functions for the GUI using the compressor classes
    def huff_compress(self,file):
        try:
            data = self.huffman.read_noncoded(f"inputs/{file}")
        except:
            self.lbl_info.config(text = "invalid file")
        self.huffman.encode_data(data)
        size1 = os.path.getsize(f"inputs/{file}")
        size2 = os.path.getsize(f"outputs/compressedhuff.txt")
        diff = (size2 / size1) * 100
        return f"file size: {round(diff)}% of original"

    def huff_decompress(self,file):
        try:
            data = self.huffman.read_encoded(f"outputs/{file}")  
        except:
            self.lbl_info.config(text = "invalid file")
        self.huffman.decode_data(data)

    def lz_compress(self,file):
        try:
            data = self.lz77.read_noncoded(f"inputs/{file}")
        except:
            self.lbl_info.config(text = "invalid file")
        self.lz77.compress(data)
        
        size1 = os.path.getsize(f"inputs/{file}")
        size2 = os.path.getsize(f"outputs/compressedlz.txt")
        diff = (size2 / size1) * 100
        return f"file size: {round(diff)}% of original"

    def lz_decompress(self,file):
        try:
            data = self.lz77.read_encoded(f"outputs/{file}")  
        except:
            self.lbl_info.config(text = "invalid file")
        self.lz77.decompress(data)
        
        

        
