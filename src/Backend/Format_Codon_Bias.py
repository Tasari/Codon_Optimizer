from .Codon import Codon
from .data import codon_to_aminoacid
from .tools import rewrite_sequence_to_codons
from ..logs import errors

def format_codon_bias(codon_bias_table):
    codons = []
    actual_codon = {'bases':'', 'frequencyper1000':'', 'amount':'', 'mode':'freq'}
    for char in codon_bias_table:
        if char in ['A', 'C', 'G', 'U']:
            actual_codon['bases'] += char
        elif char in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.'] and actual_codon['mode']=='freq':
            actual_codon['frequencyper1000'] += char 
        elif char == '(':
            actual_codon['mode'] = 'amount'
        elif char in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] and actual_codon['mode']=='amount':
            actual_codon['amount'] += char
        elif char == ')':
            codons.append(Codon(actual_codon['bases'], \
                          float(actual_codon['frequencyper1000']), \
                            int(actual_codon['amount']), \
                                codon_to_aminoacid[actual_codon['bases']]))
            actual_codon = {'bases':'', 'frequencyper1000':'', 'amount':'', 'mode':'freq'}
    codons = set_rare_codons(codons)
    return codons

def create_formatted_codon_bias_from_sequence(sequence):
    whitelist = ['A', 'C', 'G', 'U']
    codons = []
    codon_counts = {'CGA':0, 'CGC':0, 'CGG':0, 'CGU':0, 'AGA':0, 'AGG':0, 'CUA':0, 'CUC':0, 'CUG':0, 'CUU':0, 'UUA':0, 'UUG':0, 'UCA':0, 'UCC':0, 'UCG':0, 'UCU':0, 'AGC':0, 'AGU':0, 'ACA':0, 'ACC':0, 'ACG':0, 'ACU':0, 'CCA':0, 'CCC':0, 'CCG':0, 'CCU':0, 'GCA':0, 'GCC':0, 'GCG':0, 'GCU':0, 'GGA':0, 'GGC':0, 'GGG':0, 'GGU':0, 'GUA':0, 'GUC':0, 'GUG':0, 'GUU':0, 'AAA':0, 'AAG':0, 'AAC':0, 'AAU':0, 'CAA':0, 'CAG':0, 'CAC':0, 'CAU':0, 'GAA':0, 'GAG':0, 'GAC':0, 'GAU':0, 'UAC':0, 'UAU':0, 'UGC':0, 'UGU':0, 'UUC':0, 'UUU':0, 'AUA':0, 'AUC':0, 'AUU':0, 'AUG':0, 'UGG':0, 'UAA':0, 'UAG':0, 'UGA':0}
    whitelisted_sequence = ''.join([char for char in sequence.replace('T', 'U').upper() if char in whitelist])
    try:
        assert(len(whitelisted_sequence)%3 == 0)
    except AssertionError:
        errors.append("Representative sequences are not dividable by 3")
        raise Exception
    for codon in (rewrite_sequence_to_codons(whitelisted_sequence)):
        codon_counts[codon] += 1
    for key, value in codon_counts.items():
        codons.append(Codon(key, round(float(value*(len(rewrite_sequence_to_codons(whitelisted_sequence))/1000)), 1), value, codon_to_aminoacid[key]))
    codons = set_rare_codons(codons)
    return codons

def set_rare_codons(formatted_codon_bias, minimal_frequency=0.1):
    for codon in formatted_codon_bias:
        if codon.frequencyper1000 < minimal_frequency:
            codon.frequencyper1000 = minimal_frequency
    return formatted_codon_bias

