from .tools import get_most_frequent_codons


def maximize_CAI(input_aa_list, formatted_codons):
    """Returns the sequence with the most frequent codons.
    
    Takes the list of aminoacids, and creates sequence which
    codes the same protein, using only the codons which frequency
    is highest for each aminoacid.

    Args:
        input_aa_list: List of all aminoacids to rewrite in order.
        formatted_codons: List of all Codon objects.

    Returns:
        Sequence with only the most frequent codons.
    """
    most_frequent_codons = get_most_frequent_codons(formatted_codons)
    maximized_sequence = ""
    for aa in input_aa_list:
        maximized_sequence += most_frequent_codons[aa].bases
    return maximized_sequence
