from .tools import get_most_frequent_codons


def maximize_CAI(input_aa_sequence, formatted_codon_bias_table):
    most_frequent_codons = get_most_frequent_codons(formatted_codon_bias_table)
    maximized_sequence = ""
    for aa in input_aa_sequence:
        maximized_sequence += most_frequent_codons[aa].bases
    return maximized_sequence
