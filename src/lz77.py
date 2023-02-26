from bitarray import bitarray


class Lz77:

    def __init__(self):
        # Set the window size and lookahead size for the LZ77 algorithm
        self.window_size = 4095
        self.lookahead_size = 15

    def read_noncoded(self, input_file):
        # Read in a file of noncoded data and return its contents as bytes
        with open(input_file, 'rb') as file:
            data = file.read()
            return data

    def read_encoded(self, input_file):
        # Read in a file of encoded data and return its contents as a bitarray
        data = bitarray()
        with open(input_file, 'rb') as file:
            data.fromfile(file)
            return data

    def compress(self, data):
        """Compresses the input data"""
        i = 0
        compressed_data = bitarray()
        while i < len(data):
            # Find the longest match between the current position and a window of previously seen data
            match = self.find_match(data, i)
            if match:
                # If a match is found, append True to the compressed data bitarray, followed by the distance to the match and length of the match
                (distance, length, next_char) = match
                # 1 bit reserved as a flag for match
                compressed_data.append(True)
                # 16 bits reserved for distance and length of the match
                compressed_data.frombytes(bytes([distance >> 4]))
                compressed_data.frombytes(
                    bytes([((distance & 0xf) << 4) | length]))
                i += length
            else:
                # If no match is found, append False to the compressed data bitarray, followed by the next character in the data
                compressed_data.append(False)
                # 8 bits reserved for a character
                compressed_data.frombytes(bytes([data[i]]))
                i += 1
        # Fill any remaining bits in the compressed data bitarray and write the compressed data to a file
        compressed_data.fill()
        with open("files/compressedlz.txt", 'wb') as file:
            file.write(compressed_data.tobytes())

    def decompress(self, data):
        """Decompresses the input data"""
        output_data = []
        j = 0
        while len(data) >= j+9:
            flag = data[j]
            if not flag:
                # If the flag is False, the next 8 bits represent a single character, which is added to the output data
                byte = data[j+1:j+9].tobytes()
                j += 9
                output_data.append(byte)
            else:
                # If the flag is True, the next 16 bits represent the distance and length of the match, which are used to go back in the output to copy the match
                # and add it again to the output data
                byte1 = ord(data[j+1:j+9].tobytes())
                byte2 = ord(data[j+9:j+17].tobytes())
                j += 17
                distance = (byte1 << 4) | (byte2 >> 4)
                length = (byte2 & 0xf)
                for i in range(length):
                    output_data.append(output_data[-distance])
        out_data = b''.join(output_data)

        with open("files/decompressedlz.txt", 'wb') as file:
            file.write(out_data)

    def find_match(self, data, index):
        # start searching from the earliest position
        start_index = max(0, index - self.window_size)
        # search until the end of lookahead buffer
        end_index = min(index + self.lookahead_size, len(data))

        best_match_distance = -1
        best_match_length = -1

        # search for a match in the window
        for i in range(start_index, index):
            j = 0
            while index + j < end_index and data[i+j] == data[index+j]:
                j += 1
            if j > best_match_length:
                best_match_length = j
                best_match_distance = index - i
                if index + j < len(data):
                    next_char = data[index + j]
        if best_match_length > 2:  # only consider matches longer than 2 characters
            return (best_match_distance, best_match_length, next_char)
        return None
