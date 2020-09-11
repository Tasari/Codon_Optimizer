from .tools import get_most_frequent_codons


def maximize_CAI(input_aa_sequence, formatted_codons):
    most_frequent_codons = get_most_frequent_codons(formatted_codons)
    maximized_sequence = ""
    for aa in input_aa_sequence:
        maximized_sequence += most_frequent_codons[aa].bases
    return maximized_sequence
