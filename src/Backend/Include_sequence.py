from .tools import find_sequence_in_gene, rewrite_sequence_to_protein, rewrite_codons_to_sequence
from .CAI_calculation import calculate_CAI
from ..logs import errors
from itertools import product


def create_potential_sequences(sequence):
    all_sequences = []
    all_bases = ['A', 'C', 'G', 'U']
    lenght = len(sequence)
    prepared_sequences = []
    if lenght%3 != 0:
        prepared_sequences = prepare_sequences(sequence)
    else:
        prepared_sequences = [sequence]
    all_possibilities = []
    for prepared_sequence in prepared_sequences:
        all_possibilities += list(product(*[all_bases, all_bases, [prepared_sequence], all_bases]))\
                           + list(product(*[all_bases, [prepared_sequence], all_bases, all_bases]))\
                           + [prepared_sequence]
    for item in all_possibilities:
        all_sequences.append(rewrite_codons_to_sequence(item))
    return all_sequences

def prepare_sequences(sequence):
    all_sequences = []
    all_bases = ['A', 'C', 'G', 'U'] 
    if len(sequence)%3 == 1:
        all_possibilities = list(product(*[[sequence], all_bases, all_bases]))\
                          + list(product(*[all_bases, [sequence], all_bases]))\
                          + list(product(*[all_bases, all_bases, [sequence]]))
    else:
        all_possibilities = list(product(*[all_bases, [sequence]]))\
                          + list(product(*[[sequence], all_bases]))
    for item in all_possibilities:
        all_sequences.append(rewrite_codons_to_sequence(item))
    return all_sequences

def get_best_sequence(sequence, gene, formatted_codon_bias):
    rewritten_gene = rewrite_sequence_to_protein(gene)
    good_sequences = {}
    for potential in create_potential_sequences(sequence):
        if find_sequence_in_gene(rewrite_sequence_to_protein(potential), rewritten_gene) != []:
            good_sequences[potential] = calculate_CAI(potential, formatted_codon_bias)
    optimal_lenght = 1000
    for sequence in good_sequences.keys():
        if len(sequence) < optimal_lenght:
            optimal_lenght = len(sequence)
    good_keys = list(good_sequences.keys())
    for sequence in good_keys:
        if len(sequence) > optimal_lenght:
            good_sequences.pop(sequence)
    for sequence in good_sequences.keys():
        if good_sequences[sequence] == max(good_sequences.values()):
            return sequence

def include_sequence(sequence, gene, formatted_codon_bias):
    if sequence != ['']:
        if find_sequence_in_gene(sequence[0], gene) != []:
            return gene            
        try:
            best_sequence = get_best_sequence(sequence[0], gene, formatted_codon_bias)
            occurance = find_sequence_in_gene(
                            rewrite_sequence_to_protein(best_sequence),
                            rewrite_sequence_to_protein(gene))[0]*3
            final_sequence = gene[:occurance]
            final_sequence += best_sequence
            final_sequence += gene[occurance+len(best_sequence):]
            return final_sequence
        except:
            errors.append("Failed to find good place for sequence")
    return gene