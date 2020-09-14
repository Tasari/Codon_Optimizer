from .data import codon_to_aminoacid
import re


def rewrite_to_rna(sequence):
    """Returns sequence rewritten to RNA and in upper letters."""
    sequence = sequence.replace("T", "U").replace("\n", "").upper()
    return sequence


def rewrite_sequence_to_protein(sequence):
    """Returns sequence of aminoacids symbolizing protein from sequence."""
    return rewrite_codons_to_protein(rewrite_sequence_to_codons(sequence))


def rewrite_sequence_to_codons(sequence):
    """Returns list of codons created from the sequence."""
    codons = []
    base = 0
    for _ in range(int(len(sequence) / 3)):
        codons.append(sequence[base] + sequence[base + 1] + sequence[base + 2])
        base += 3
    return codons


def rewrite_sequence_to_aminoacids(sequence):
    """Returns list of aminoacids created from sequence."""
    return rewrite_codons_to_aminoacids(rewrite_sequence_to_codons(sequence))


def rewrite_codons_to_sequence(codons):
    """Returns sequence created from list of codons."""
    sequence = ""
    for codon in codons:
        sequence += codon
    return sequence


def rewrite_codons_to_protein(codons):
    """Returns protein sequence created from list of codons"""
    protein = ""
    for codon in codons:
        protein += codon_to_aminoacid[codon]
    return protein


def rewrite_codons_to_aminoacids(codons):
    """Creates list of ordered aminoacids from codons list"""
    aminoacids = []
    for codon in codons:
        aminoacids.append(codon_to_aminoacid[codon])
    return aminoacids


def get_most_frequent_codons(formatted_codons):
    """Returns the dict of most frequent codons coding each aminoacid.
    
    Creates dictionary where to each aminoacid, being key, the codon
    coding this aminoacid and with highest frequency is connected
    based on list of Codon objects.
    """

    optimal_codon = {}
    for codon in formatted_codons:
        if codon.aminoacid not in optimal_codon.keys():
            optimal_codon[codon.aminoacid] = codon
        elif optimal_codon[codon.aminoacid].frequencyper1000 < codon.frequencyper1000:
            optimal_codon[codon.aminoacid] = codon
    return optimal_codon


def find_sequence_in_gene(sequence, gene):
    """Returns list of starts of occurances of sequence in gene"""
    return [
        found.start()
        for found in re.finditer(re.compile(rewrite_to_rna(sequence)), gene)
    ]


def create_codon_bias_supersequence(formatted_codons):
    """Creates string containing each codon times this codon's amount"""
    superstring = ""
    for codon in formatted_codons:
        superstring += codon.bases * codon.amount
    return superstring
