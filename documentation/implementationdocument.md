## Implementation document

### Structure
Program consists of classes huffman and lz77, which house their respective compression algorithms. The UI class houses the interface the user will be using the program with.

#### Huffman
In Huffman class the compression takes an input file and creates a frequency tablebased on the frequency of the characters in the text, the frequency table is then used to create a huffman tree, the tree is then used to build a dictionary of characters and their respective bits. The dictionary then is used to encode the text itself, and the encoded text(and the extra bits needed to make it divisible by 8 as required by bytefiles) and the dictionary are saved into a file.
The decompression reverses the process, reading the file, and using the dictionary to convert the text into readeble form. Uses the Huffman tree which is a binary tree, thus the time complexity is O(nlogn).

#### LZ77
In lz77 class the compression takes an input file, reads it, and starts looping through the data looking for matching repeats. This is done by using a sliding window of 4095 characters backwards, and 15 characters forwards. The longest repeating line that is found in both windows is then saved as a match in the form of(distance, length) and coded into a file with a flag indicating that it is a match, if no match for a certain start point character is found, the character itself is saved into the file, along with a flag to indicate that it is not a match. The decompression function builds the original text back from the lone characters and matches, using the distance and length to look back at the already build text to copy the contents of a match into the current end of the output. The time complexity is technically O(n) but its actually O(n*w) where w is window size.