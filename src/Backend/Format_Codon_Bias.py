from .Codon import Codon
from .data import codon_to_aminoacid
def format_codon_bias(codon_bias_table):
    split_table=codon_bias_table.split()
    codons = []
    place = 0
    for i in range(int(len(split_table)/3)):
        codons.append(Codon(split_table[place], \
                            split_table[place+1][:-1], \
                            split_table[place+2][:-1], \
                            codon_to_aminoacid[split_table[place]]))
        place+=3
    codons = set_rare_codons(codons)
    return codons

def set_rare_codons(formatted_codon_bias, minimal_frequency=0.1):
    for codon in formatted_codon_bias:
        if codon.frequencyper1000 < minimal_frequency:
            codon.frequencyper1000 = minimal_frequency
    return formatted_codon_bias