## Implementation document

### Structure
Program consists of classes huffman and lz77, which house their respective compression algorithms. The UI class houses the interface the user will be using the program with.

#### Huffman
The huffman class: 
1. Takes an input file and reads it.
2. Creates a frequency table based on the frequency of the characters in the text.
3. The frequency table is then used to create a huffman tree.
4. The tree is then used to build a dictionary of characters and their respective bits.
5. The dictionary then is used to encode the text itself
6. The encoded text(and the extra bits needed to make it divisible by 8 as required by byte files) and the dictionary are saved into a file.
7. The decompression reverses the process, reading the file, and using the dictionary to convert the text into readable form.

Bitarray module is used to save the data as bits and for the simple encoding of the data. 

 Uses the Huffman tree which is a binary tree, thus the time complexity is O(nlogn).

#### LZ77
In lz77 class:
1. Takes an input file and reads it.
2. Starts looping through the data looking for matching repeats. This is done by using a sliding window of 4095 characters backwards, and 15 characters forwards.
3. The longest repeating line that is found in both windows is then saved as a match in the form of(distance, length) and coded into a file with a flag indicating that it is a match.
4. If no match for a certain start point character is found, the character itself is saved into the file, along with a flag to indicate that it is not a match.
5. The decompression function builds the original text back from the lone characters and matches, using the distance and length to look back at the already build text to copy the contents of a match into the current end of the output.

Unlike the original LZ77 algorithm where the next character was saved with distance and length, the character is omitted from the file to save space and instead a flag bit is used to tell the decompressor if the next input is a match or not. This also lets the algorithm to only save the character with no match in the file instead of saving multiple zeroes.

Bitarray module is used to save the data as bits since I was already using it for Huffman class.

The time complexity is O(n*w) where w is window size.
