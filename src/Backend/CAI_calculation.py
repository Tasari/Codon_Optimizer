from math import exp, fsum, log
from .tools import get_most_frequent_codons, rewrite_sequence_to_codons

def calculate_CAI(data, formatted_codon_bias_table):
    to_count = []
    codon_freq_aa = reformat_table_codon_freq_aa(formatted_codon_bias_table)
    forbidden = ['UGG', 'AUG', 'UAA', 'UGA', 'UAG']
    most_freq_codons = get_most_frequent_codons(formatted_codon_bias_table)
    for codon in rewrite_sequence_to_codons(data):
        if codon in forbidden:
            continue
        best_codon_freq = most_freq_codons[codon_freq_aa[codon][1]].frequencyper1000
        to_count.append(codon_freq_aa[codon][0]/best_codon_freq)
    return round(geomean(to_count), 3)

def reformat_table_codon_freq_aa(formatted_codon_bias):
    codon_freq = {}
    for codon in formatted_codon_bias:
        codon_freq[codon.bases] = (codon.frequencyper1000, codon.aminoacid)
    return codon_freq

def geomean(xs):
    return exp(fsum(log(x) for x in xs) / len(xs))