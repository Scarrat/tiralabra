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

Unlike the original LZ77 algorithm where the next character was saved with distance and length, the character is omitted from the file to save space and instead a flag bit is used to tell the decompressor if the next input is a match or not. This also lets the algorithm to only save the character with no match in the file instead of saving multiple zeroes. This is more like LZSS. I opted to use this approach since for some reason I could not seem to be able to find a way to make the original LZ77 work within the compression parameter of under 60%, or I had other issues with bytes/characters.

Bitarray module is used to save the data as bits since I was already using it for Huffman class and a guide I followed used it.

The time complexity for the lz compression is O(n), but since the search algorithm complexity is O(n * w) where w is the window size, the total time complexity is O(n * w). Testing data seems to prove this since it takes a lot longer than the huffman algorithm.

### Comparison

Huffman algorithm seems generally decent at compression, mostly staying under 60% size. At very small file sizes the dictionary itself adds most of the extra size which lessens the effect as the file itself grows. Speed is very fast, since it basically only needs to do translating.

Lempel-Ziv has better compression at small sizes due to no dictionary, and seems to be better at higher file sizes too, though at a big hit to speed. Also seems to hate randomly generated text in which speed takes a big hit and compression is awful. As seen in the testing data, most of the time comes unsurpisingly from the search algorithm which needs to repeat the window for every character.

Specific data below.

##### Huffman
![file1](https://github.com/Scarrat/tiralabra/blob/main/documentation/imgs/Screenshot_20230312_185823.png)

###### Compressing
| File  | Process time | Percentage of original |
| ------------- | ------------- |------------- |
| 5kb lorem  | 0.006 s  | 73% |
| 10kb lorem  | 0.008 s  | 64%  |
| 50kb lorem  | 0.03 s  | 56%  |
| 100kb lorem  | 0.05 s  | 55%  |
| 144kb random  | 0.03 s  | 60%  |
| 144kb shakespeare  | 0.05 s  | 61%  |
| 1.2mb moby dick  | 0.2 s  | 56%  |

###### Decompressing
| File  | Process time | 
| ------------- | ------------- |
| 5kb lorem  | 0.003 s  | 
| 10kb lorem  | 0.003 s  | 
| 50kb lorem  | 0.01 s  | 
| 100kb lorem  | 0.02 s  | 
| 144kb random  | 0.03 s  | 
| 144kb shakespeare  | 0.03 s | 
| 1.2mb moby dick  | 0.08 s  |



#### Lempel-Ziv

![file2](https://github.com/Scarrat/tiralabra/blob/main/documentation/imgs/Screenshot_20230312_185849.png)
###### Compressing
| File  | Process time | Percentage of original |
| ------------- | ------------- |------------- |
| 5kb lorem  | 0.4 s  | 46% |
| 10kb lorem  | 0.9 s  | 39%  |
| 50kb lorem  | 5.1 s  | 34%  |
| 100kb lorem  | 10.7 s  | 34%  |
| 144kb random  | 64.9 s  | 94%  |
| 144kb shakespeare  | 27.2 s  | 53%  |
| 1.2mb moby dick  | 254.6 s  | 54%  |

###### Decompressing
| File  | Process time | 
| ------------- | ------------- |
| 5kb lorem  | 0.007 s  | 
| 10kb lorem  | 0.01 s  | 
| 50kb lorem  | 0.03 s  | 
| 100kb lorem  | 0.05 s  | 
| 144kb random  | 0.09 s  | 
| 144kb shakespeare  | 0.08 s | 
| 1.2mb moby dick  | 0.4 s  |


### Improvements
LZ algorithm search could be optimized with a variable window, might make it faster on specific files. Huffman algorithm could use a better way to store the dictionary into the file rather than just plain text, effect negligible on bigger files though.

### Sources
http://ilan.schnell-web.net/prog/huffman/ for help with huffman algorithm.   
https://blog.finxter.com/python-join-list-of-bytes/ for help with bytes.  
https://pypi.org/project/bitarray/ for the bitarray module.  
https://stackoverflow.com/ for multiple tips and tricks and explanations.  
https://timguite.github.io/jekyll/update/2020/03/15/lz77-in-python.html for help with lz.  
https://www.geeksforgeeks.org/python-bitwise-operators/ for help with bit operations  
https://tim.cogan.dev/lzss/ for guidance with the lz compression function.  
https://blog.sentry.io/2022/09/30/python-performance-testing-a-comprehensive-guide/ for help with performance testing.   
