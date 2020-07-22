def get_most_frequent_codons(formatted_gene_bias_table):
    optimal_codon = {}
    for codon in formatted_gene_bias_table:
        if codon.aminoacid not in optimal_codon.keys():
            optimal_codon[codon.aminoacid] = codon
        elif optimal_codon[codon.aminoacid].frequencyper1000<codon.frequencyper1000:
            optimal_codon[codon.aminoacid] = codon
    return optimal_codon        

def maximize_CAI(input_aa_sequence, formatted_gene_bias_table):
    most_frequent_codons=get_most_frequent_codons(formatted_gene_bias_table)
    maximized_sequence = ''
    for aa in input_aa_sequence:
        maximized_sequence += most_frequent_codons[aa].bases
    return maximized_sequence