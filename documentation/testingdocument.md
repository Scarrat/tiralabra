## Testing document

Unittesting report [![codecov](https://codecov.io/gh/Scarrat/tiralabra/branch/main/graph/badge.svg?token=KXH4PSGWHR)](https://codecov.io/gh/Scarrat/tiralabra)  

### Unittests
Both classes have similar unittests testing the readability of compressed and uncompressed files, compressing and decompressing back to original text, and testing the compression rate of 100kb lorem ipsum file so it is under 60%.
Tests can be run by using `poetry run pytest` on the src directory.
Report can be found here: ![codecov](https://codecov.io/gh/Scarrat/tiralabra/branch/main/graph/badge.svg?token=KXH4PSGWHR)


### Performance testing

Performance testing was done with specific perftest.py file. The process was checked by using cProfile with a 100kb lorem ipsum file.


#### Huffman
##### Compressing
| File  | Process time | Percentage of original |
| ------------- | ------------- |------------- |
| 5kb lorem  | 0.006 s  | 73% |
| 10kb lorem  | 0.008 s  | 64%  |
| 50kb lorem  | 0.03 s  | 56%  |
| 100kb lorem  | 0.05 s  | 55%  |
| 144kb random  | 0.03 s  | 60%  |
| 144kb shakespeare  | 0.05 s  | 61%  |
| 1.2mb moby dick  | 0.2 s  | 56%  |
##### Decompressing
| File  | Process time | 
| ------------- | ------------- |
| 5kb lorem  | 0.003 s  | 
| 10kb lorem  | 0.003 s  | 
| 50kb lorem  | 0.01 s  | 
| 100kb lorem  | 0.02 s  | 
| 144kb random  | 0.03 s  | 
| 144kb shakespeare  | 0.03 s | 
| 1.2mb moby dick  | 0.08 s  |

Huffman algorithm seems generally decent at compression, mostly staying under 60% size. At very small file sizes the dictionary itself adds most of the extra size which lessens the effect as the file itself grows. Speed is very good.

#### Lempel-Ziv
##### Compressing
| File  | Process time | Percentage of original |
| ------------- | ------------- |------------- |
| 5kb lorem  | 0.4 s  | 46% |
| 10kb lorem  | 0.9 s  | 39%  |
| 50kb lorem  | 5.1 s  | 34%  |
| 100kb lorem  | 10.7 s  | 34%  |
| 144kb random  | 64.9 s  | 94%  |
| 144kb shakespeare  | 27.2 s  | 53%  |
| 1.2mb moby dick  | 254.6 s  | 54%  |

##### Decompressing
| File  | Process time | 
| ------------- | ------------- |
| 5kb lorem  | 0.007 s  | 
| 10kb lorem  | 0.01 s  | 
| 50kb lorem  | 0.03 s  | 
| 100kb lorem  | 0.05 s  | 
| 144kb random  | 0.09 s  | 
| 144kb shakespeare  | 0.08 s | 
| 1.2mb moby dick  | 0.4 s  |

Lempel-Ziv has better compression at small sizes due to no dictionary, and seems to be better at higher file sizes too, though at a big hit to speed. Also seems to hate randomly generated text in which speed takes a big hit and compression is awful.



