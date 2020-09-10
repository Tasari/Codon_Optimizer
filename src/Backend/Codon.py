class Codon:
    def __init__(self, bases, frequencyper1000, amount, aminoacid):
        self.bases = bases
        self.frequencyper1000 = float(frequencyper1000)
        self.amount = int(amount)
        self.aminoacid = aminoacid

    def __repr__(self):
        return "Codon_obj('{}')".format(self.bases)
