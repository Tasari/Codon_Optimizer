import re
from .tools import find_sequence_in_gene, rewrite_sequence_to_protein, rewrite_codons_to_sequence
from .CAI_calculation import calculate_CAI
from ..logs import errors
from itertools import product


def create_potential_sequences(sequence):
    all_sequences = []
    all_bases = ['A', 'C', 'G', 'U']
    lenght = len(sequence)
    if lenght%3 == 0:
        all_sequences.append(sequence)
    elif lenght%3 == 1:
        [all_sequences.append(rewrite_codons_to_sequence(item)) for item in product(*[sequence,all_bases, all_bases])]
        [all_sequences.append(rewrite_codons_to_sequence(item)) for item in product(*[all_bases, sequence, all_bases])]
        [all_sequences.append(rewrite_codons_to_sequence(item)) for item in product(*[all_bases, all_bases, sequence])]
    else:
        [all_sequences.append(rewrite_codons_to_sequence(item)) for item in product(*[all_bases, [sequence]])]
        [all_sequences.append(rewrite_codons_to_sequence(item)) for item in product(*[[sequence], all_bases])]
    return all_sequences

def get_best_sequence(sequence, gene, formatted_codon_bias):
    rewritten_gene = rewrite_sequence_to_protein(gene)
    good_sequences = {}
    for potential in create_potential_sequences(sequence):
        if find_sequence_in_gene(rewrite_sequence_to_protein(potential), rewritten_gene) != []:
            good_sequences[calculate_CAI(potential, formatted_codon_bias)] = potential
    return good_sequences[max(good_sequences.keys())]

def include_sequence(sequence, gene, formatted_codon_bias):
    if sequence != ['']:
        if find_sequence_in_gene(sequence[0], gene) != []:
            return gene            
        try:
            occurance = find_sequence_in_gene(rewrite_sequence_to_protein(get_best_sequence(sequence, gene, formatted_codon_bias)), rewrite_sequence_to_protein(gene))[0]*3
            final_sequence = gene[0:occurance]
            final_sequence += sequence[0]
            final_sequence += gene[occurance+len(sequence[0]):]
            return final_sequence
        except:
            errors.append("Failed to find good place for sequence")
    return gene