class FastaRecord:
    """
    Fasta Record, contains a header and a sequence
    """
    def __init__(self, header="", sequence=""):
        self.header = header
        self.sequence = sequence

    def __str__(self):
        return ">{}\n{}".format(self.header, self.sequence)


def fasta_iterator(fasta_handle):
    """
    Generate FastaRecords from a handle to a fasta file

    :param fasta_handle: Open, readable handle to a file-like object
    :yield: A FastaRecord for each record in fasta_handle
    """
    rec = None
    for line in fasta_handle:
        if line[0] == '>':
            if rec:
                yield rec
            rec = FastaRecord(line.strip()[1:])
        else:
            rec.sequence += line.strip()

    if rec:
        yield rec
