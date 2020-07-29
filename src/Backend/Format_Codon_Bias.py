from .Codon import Codon
from .data import codon_to_aminoacid
def format_codon_bias(codon_bias_table):
    codons = []
    codon = ''
    frequencyper1000 = ''
    amount = ''
    mode = 'freq'
    for char in codon_bias_table:
        if char in ['A', 'C', 'G', 'U']:
            codon+=char
        elif char in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.'] and mode=='freq':
            frequencyper1000 += char 
        elif char == '(':
            mode = 'amount'
        elif char in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] and mode=='amount':
            amount+=char
        elif char == ')':
            codons.append(Codon(codon, float(frequencyper1000),int(amount),codon_to_aminoacid[codon]))
            codon = ''
            frequencyper1000 = ''
            amount = ''
            mode = 'freq'
    codons = set_rare_codons(codons)
    return codons

def set_rare_codons(formatted_codon_bias, minimal_frequency=0.5):
    for codon in formatted_codon_bias:
        if codon.frequencyper1000 < minimal_frequency:
            codon.frequencyper1000 = minimal_frequency
    return formatted_codon_bias