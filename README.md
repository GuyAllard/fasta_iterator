Fasta Iterator
==============
A very simple python iterator for parsing fasta files


**Installation**  
from within this directory, run  
```
pip install .
```


**Usage**  
```python
from fasta_iterator import fasta_iterator  
with open("somefile.fasta", "r") as fasta:
    for record in fasta_iterator(fasta):
        print(record.header)
        print(record.sequence)
```
