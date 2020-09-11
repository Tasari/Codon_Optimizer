class Codon:
    """Class holding data about codon.

    Attributes:
        bases: 
            String of bases of each codon.
        frequencyper1000: 
            Float indicating amount of codon occurances per 1000 codons.
        amount:
            Integer count of occurances in representative data.
        aminoacid:
            Char letter symbol of aminoacid coded by bases.
    """
    def __init__(self, bases, frequencyper1000, amount, aminoacid):
        """Inits Codon with given arguments"""
        self.bases = bases
        self.frequencyper1000 = float(frequencyper1000)
        self.amount = int(amount)
        self.aminoacid = aminoacid

    def __repr__(self):
        """Representatnion of codon"""
        return "Codon_obj('{}')".format(self.bases)
