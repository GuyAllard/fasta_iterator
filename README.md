Fasta Iterator
==============
A very simple python iterator for parsing fasta files


**Installation**  
To install with pip, run
```
pip install https://github.com/guyallard/fasta_iterator/archive/v1.0.0.zip
```


**Usage**  
```python
from fasta_iterator import fasta_iterator  
with open("somefile.fasta", "r") as fasta:
    for record in fasta_iterator(fasta):
        print(record.header)
        print(record.sequence)
```
