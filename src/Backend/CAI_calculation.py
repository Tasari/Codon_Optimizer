from math import exp, fsum, log
from .tools import get_most_frequent_codons, rewrite_sequence_to_codons


def calculate_CAI(data, formatted_codons):
    """Calculates and returns calculated CAI score.

    Collects ratio of each codon frequency/most frequent codon 
    frequency and returns geometric mean of all the ratios
    which is CAI score.
    
    Args:
        data: Sequence which CAI we want to calculate.
        formatted_codons: List of formatted codons.

    Returns:
        Float CAI score, CAI = 1 is max, when all codons 
        are most frequent ones.
    """
    to_count = []
    codon_freq_aa = reformat_table_codon_freq_aa(formatted_codons)
    forbidden = ["UGG", "AUG", "UAA", "UGA", "UAG"]
    most_freq_codons = get_most_frequent_codons(formatted_codons)
    for codon in rewrite_sequence_to_codons(data):
        if codon in forbidden:
            continue
        best_codon_freq = most_freq_codons[codon_freq_aa[codon][1]].frequencyper1000
        to_count.append(codon_freq_aa[codon][0] / best_codon_freq)
    return round(geomean(to_count), 3)


def reformat_table_codon_freq_aa(formatted_codon_bias):
    """Returns dict mapping "bases":(frequency, "aminoacid").

    Takes data from formatted codon bias and creates dict
    "bases":(frequency, "aminoacid").

    Args:
        formatted_codon_bias: List of formatted codons.
    """
    codon_freq = {}
    for codon in formatted_codon_bias:
        codon_freq[codon.bases] = (codon.frequencyper1000, codon.aminoacid)
    return codon_freq


def geomean(xs):
    """Returns geometric mean of list."""
    return exp(fsum(log(x) for x in xs) / len(xs))
