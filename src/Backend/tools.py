from .data import codon_to_aminoacid
def rewrite_sequence_to_protein(sequence):
    return rewrite_codons_to_protein(rewrite_sequence_to_codons(sequence))

def rewrite_sequence_to_codons(sequence):
    codons=[]
    base=0
    for i in range(int(len(sequence)/3)):
        codons.append(sequence[base]+sequence[base+1]+sequence[base+2])
        base += 3
    return codons
    
def rewrite_sequence_to_aminoacids(sequence):
    return rewrite_codons_to_aminoacids(rewrite_sequence_to_codons(sequence))

def rewrite_codons_to_sequence(codons):
    sequence = ''
    for codon in codons:
        sequence += codon
    return sequence

def rewrite_codons_to_protein(codons):
    protein = ''
    for codon in codons:
        protein += codon_to_aminoacid[codon]
    return protein

def rewrite_codons_to_aminoacids(codons):
    aminoacids=[]
    for codon in codons:
        aminoacids.append(codon_to_aminoacid[codon])
    return aminoacids

def get_most_frequent_codons(formatted_codon_bias_table, n=1):
    optimal_codon = {}
    if n != 1:
        final_table = get_limited_table(formatted_codon_bias_table, n)
    else:
        final_table = formatted_codon_bias_table
    for codon in final_table:
        if codon.aminoacid not in optimal_codon.keys():
            optimal_codon[codon.aminoacid] = codon
        elif optimal_codon[codon.aminoacid].frequencyper1000<codon.frequencyper1000:
            optimal_codon[codon.aminoacid] = codon
    return optimal_codon        

def get_limited_table(formatted_codon_bias_table, n):
    all_codons = formatted_codon_bias_table[:]
    backup = all_codons[:]

    for i in range(n-1):
        for value in get_most_frequent_codons(all_codons).values():
            all_codons.remove(value)
    all_aminoacids = [codon.aminoacid for codon in all_codons]
    
    for codon in backup:
        if codon.aminoacid not in all_aminoacids:
            all_codons.append(codon)
    return get_most_frequent_codons(all_codons).values()

