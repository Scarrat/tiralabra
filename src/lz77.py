from bitarray import bitarray


class Lz77:
    """Badly in progress, here be spaghetti"""

    def __init__(self):
        self.window = 200
        self.lookahead = 15

    def read_noncoded(self,input_file):
        with open(input_file, 'rb') as input_file:
            data = input_file.read()
            return data

    def read_encoded(self,input_file):
        data = bitarray()
        with open(input_file, 'rb') as input_file:
            data.fromfile(input_file)
            return data
    
    def compress(self,data):
        i = 0
        while i < len(data):
            print("ix2")
            match = self.search_match(data, i)
            
            if match:
                (dist, length) = match
                i+=length


            i+= i



    def search_match(self, data, index):
        """searches best possible match for string starting from index inside lookahead"""
        buffer = min(index + self.lookahead, len(data) + 1)
        best_dist = -1
        best_len= -1

        # for i in range(index+2, buffer):

        #     print("i")
        #     start = max(0, index - self.window)
        #     substring = data[index:i]
            
        #     for j in range(start, index):
        #         print("j")
        #         if j + i <= len(data):
        #             string = data[j:j+i]
                
        #         if string == substring and len(substring) > best_len:
        #             best_dist = index - i 
        #             best_len = len(substring)

        # if best_dist > 0 and best_len > 0:
        #     return (best_dist, best_len)
        # return None
                
            


