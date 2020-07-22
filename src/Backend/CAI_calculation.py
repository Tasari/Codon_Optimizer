from math import exp, fsum, log
from .tools import get_most_frequent_codons, rewrite_sequence_to_codons

def geomean(xs):
    return exp(fsum(log(x) for x in xs) / len(xs))

def calculate_CAI(data, formatted_codon_bias_table):
    sequence = data.all_data().replace("T", 'U').replace('\n', '')
    to_count=[]
    dicto_testo = {}
    total = 0
    most_frequent_codons = get_most_frequent_codons(formatted_codon_bias_table)
    for codon in formatted_codon_bias_table:
        total += codon.amount
        if codon not in dicto_testo.keys():
            dicto_testo[codon.bases] = codon
    for codon in rewrite_sequence_to_codons(sequence):
        if dicto_testo[codon].frequencyper1000 < 0.51:
            w = dicto_testo[codon].amount/total*1000/most_frequent_codons[dicto_testo[codon].aminoacid].frequencyper1000 
        else:
            w = dicto_testo[codon].frequencyper1000/most_frequent_codons[dicto_testo[codon].aminoacid].frequencyper1000
        if w != 0:
            to_count.append(w)
    result = round(geomean(to_count), 3)
    data.set_CAI(result)
    return result