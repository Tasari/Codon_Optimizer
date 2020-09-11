from .data import codon_to_aminoacid
import re


def rewrite_to_rna(sequence):
    sequence = sequence.replace("T", "U").replace("\n", "").upper()
    return sequence


def rewrite_sequence_to_protein(sequence):
    return rewrite_codons_to_protein(rewrite_sequence_to_codons(sequence))


def rewrite_sequence_to_codons(sequence):
    codons = []
    base = 0
    for i in range(int(len(sequence) / 3)):
        codons.append(sequence[base] + sequence[base + 1] + sequence[base + 2])
        base += 3
    return codons


def rewrite_sequence_to_aminoacids(sequence):
    return rewrite_codons_to_aminoacids(rewrite_sequence_to_codons(sequence))


def rewrite_codons_to_sequence(codons):
    sequence = ""
    for codon in codons:
        sequence += codon
    return sequence


def rewrite_codons_to_protein(codons):
    protein = ""
    for codon in codons:
        protein += codon_to_aminoacid[codon]
    return protein


def rewrite_codons_to_aminoacids(codons):
    aminoacids = []
    for codon in codons:
        aminoacids.append(codon_to_aminoacid[codon])
    return aminoacids


def get_most_frequent_codons(formatted_codons):
    optimal_codon = {}
    for codon in formatted_codons:
        if codon.aminoacid not in optimal_codon.keys():
            optimal_codon[codon.aminoacid] = codon
        elif optimal_codon[codon.aminoacid].frequencyper1000 < codon.frequencyper1000:
            optimal_codon[codon.aminoacid] = codon
    return optimal_codon


def find_sequence_in_gene(sequence, gene):
    found_indexes = [
        found.start()
        for found in re.finditer(re.compile(rewrite_to_rna(sequence)), gene)
    ]
    return found_indexes


def create_codon_bias_supersequence(formatted_codons):
    superstring = ""
    for codon in formatted_codons:
        superstring += codon.bases * codon.amount
    return superstring
