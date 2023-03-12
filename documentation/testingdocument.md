## Testing document

Unittesting report [![codecov](https://codecov.io/gh/Scarrat/tiralabra/branch/main/graph/badge.svg?token=KXH4PSGWHR)](https://codecov.io/gh/Scarrat/tiralabra)  

### Unittests
Both classes have similar unittests testing the readability of compressed and uncompressed files, compressing and decompressing back to original text, and testing the compression rate of 100kb lorem ipsum file so it is under 60%.
Tests can be run by using `poetry run pytest` on the src directory.
Report can be found here: ![codecov](https://codecov.io/gh/Scarrat/tiralabra/branch/main/graph/badge.svg?token=KXH4PSGWHR)


### Performance testing

Performance testing was done with specific perftest.py file. cProfile was used on a 100kb file to see the specific time usages and different size performance can be manually checked. Tests can be done by running `poetry run python3 perftest.py` in src directory. Refer to implementation document for  comparison

##### Huffman
cProfile used with 100kb file.   
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
cProfile used with 100kb file.   
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

