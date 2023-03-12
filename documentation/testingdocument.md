## Testing document

Unittesting report [![codecov](https://codecov.io/gh/Scarrat/tiralabra/branch/main/graph/badge.svg?token=KXH4PSGWHR)](https://codecov.io/gh/Scarrat/tiralabra)  

### Unittests
Both classes have similar unittests testing the readability of compressed and uncompressed files, compressing and decompressing back to original text, and testing the compression rate of 100kb lorem ipsum file so it is under 60%.
Tests can be run by using `poetry run pytest` on the src directory.
Report can be found here: ![codecov](https://codecov.io/gh/Scarrat/tiralabra/branch/main/graph/badge.svg?token=KXH4PSGWHR)


### Performance testing

Performance testing was done with specific perftest.py file. cProfile was used on a 100kb file to see the specific time usages and different size performance can be manually checked. Tests can be done by running `poetry run python3 perftest.py` in src directory. Refer to implementation document for results and comparison


