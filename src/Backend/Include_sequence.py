from .tools import find_sequence_in_gene, rewrite_sequence_to_protein, rewrite_codons_to_sequence
from .CAI_calculation import calculate_CAI
from ..logs import errors
from itertools import product


def create_potential_sequences(sequence):
    all_sequences = []
    all_bases = ['A', 'C', 'G', 'U']
    all_possibilities = []
    if len(sequence) % 3 != 0:
        prepared_sequences = prepare_sequences(sequence)
    else:
        prepared_sequences = [sequence]
    for prepared_sequence in prepared_sequences:
        all_possibilities += list(product(*[all_bases, all_bases,\
                                            [prepared_sequence], all_bases]))\
                           + list(product(*[all_bases, [prepared_sequence], \
                                            all_bases, all_bases]))\
                           + [prepared_sequence]
    for item in all_possibilities:
        all_sequences.append(rewrite_codons_to_sequence(item))
    return all_sequences

def prepare_sequences(sequence):
    all_sequences = []
    all_bases = ['A', 'C', 'G', 'U'] 
    if len(sequence) % 3 == 1:
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
        if find_sequence_in_gene(rewrite_sequence_to_protein(potential), \
                                 rewritten_gene) != []:
            good_sequences[potential] = calculate_CAI(potential, \
                                                      formatted_codon_bias)
    shortest_good_sequences = erase_not_shortest_sequences(good_sequences)
    for sequence in shortest_good_sequences.keys():
        if good_sequences[sequence] == max(shortest_good_sequences.values()):
            return sequence

def erase_not_shortest_sequences(good_sequences):
    optimal_lenght = 2147483646
    good_keys = list(good_sequences.keys())
    for sequence in good_keys:
        if len(sequence) < optimal_lenght:
            optimal_lenght = len(sequence)
    for sequence in good_keys:
        if len(sequence) > optimal_lenght:
            good_sequences.pop(sequence)
    return good_sequences

def include_sequence(sequence, gene, formatted_codon_bias):
    if sequence != ['']:
        if find_sequence_in_gene(sequence[0], gene) != []:
            errors.append("Sequence already in gene")
            return gene            
        try:
            final_sequence = build_gene_with_sequence(sequence, gene, \
                                                      formatted_codon_bias)
            return final_sequence
        except:
            errors.append("Failed to find good place for sequence")
    return gene

def build_gene_with_sequence(sequence, gene, formatted_codon_bias):
    best_sequence = get_best_sequence(sequence[0], gene, \
                                      formatted_codon_bias)
    occurance = find_sequence_in_gene(
                    rewrite_sequence_to_protein(best_sequence),
                    rewrite_sequence_to_protein(gene))[0] * 3
    remade_sequence = gene[:occurance]
    remade_sequence += best_sequence
    remade_sequence += gene[occurance + len(best_sequence):]
    return remade_sequence