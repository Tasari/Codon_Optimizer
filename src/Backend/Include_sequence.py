from .tools import (
    find_sequence_in_gene,
    rewrite_sequence_to_protein,
    rewrite_codons_to_sequence,
)
from .CAI_calculation import calculate_CAI
from ..logs import errors
from itertools import product


def include_sequence(sequence, gene, formatted_codons):
    """Includes sequence into gene keeping the protein sequence.

    If sequence not in gene it tries to find good place for
    sequence and put it into the gene.

    Args:
        sequence: 
            List of sequences to be inclueded for now only
            accepts list with one sequence.
        gene:
            Gene string in which we want to have the sequence.
        formatted_codons: List of Codon objects.
        
    Returns:
        Gene with included sequence if successfull,
        and input gene if including failed.
    """
    if sequence != [""]:
        if find_sequence_in_gene(sequence[0], gene) != []:
            errors.append("Sequence already in gene")
            return gene
        try:
            final_sequence = build_gene_with_sequence(
                sequence, gene, formatted_codons
            )
            return final_sequence
        except:
            errors.append("Failed to find good place for sequence")
    return gene


def build_gene_with_sequence(sequence, gene, formatted_codons):
    """Tries to rebuild gene to contain the sequence.

    Creates sequence which fits in the gene, and puts it
    into the gene keeping the protein.

    Args:
        sequence: Secuence we want to be included.
        gene: Gene to be edited.
        formatted_codons: List of Codon objects.

    Returns:
        Sequence with included sequence if succesfull
        or raises exception catched in higher level.
    """
    best_sequence = get_best_sequence(sequence[0], gene, formatted_codons)
    occurance = (
        find_sequence_in_gene(
            rewrite_sequence_to_protein(best_sequence),
            rewrite_sequence_to_protein(gene),
        )[0]
        * 3
    )
    remade_sequence = gene[:occurance]
    remade_sequence += best_sequence
    remade_sequence += gene[occurance + len(best_sequence) :]
    return remade_sequence


def get_best_sequence(sequence, gene, formatted_codons):
    """Returns the best potential sequence based on CAI and lenght.
    
    Rewrites all the potential sequences to protein and if combination
    is found in the rewritten gene it accepts it as good sequence,
    calculating its CAI and removing all those which were not shortest 
    possible, then returning the one with highest CAI score.

    Args:
        sequence: Secuence we want to be included.
        gene: Gene to be edited.
        formatted_codons: List of Codon objects.
    
    Returns:
        Fitting sequence with highest CAI.
    """
    rewritten_gene = rewrite_sequence_to_protein(gene)
    good_sequences = {}
    for potential in create_potential_sequences(sequence):
        if (
            find_sequence_in_gene(
                rewrite_sequence_to_protein(potential), rewritten_gene
            )
            != []
        ):
            good_sequences[potential] = calculate_CAI(potential, formatted_codons)
    shortest_good_sequences = erase_not_shortest_sequences(good_sequences)
    for sequence in shortest_good_sequences.keys():
        if good_sequences[sequence] == max(shortest_good_sequences.values()):
            return sequence


def create_potential_sequences(sequence):
    """Creates potential sequences containing target sequence.
    
    Creates sequences with target sequence in all possible places
    creating multiple different protein combinations containing
    the target sequence.

    Args:
        sequence: Sequence on which we want to create potential ones.

    Returns:
        List of all potential sequences.
    """
    all_sequences = []
    all_bases = ["A", "C", "G", "U"]
    all_possibilities = []
    if len(sequence) % 3 != 0:
        prepared_sequences = prepare_sequences(sequence)
    else:
        prepared_sequences = [sequence]
    for prepared_sequence in prepared_sequences:
        all_possibilities += (
            list(product(*[all_bases, all_bases, [prepared_sequence], all_bases]))
            + list(product(*[all_bases, [prepared_sequence], all_bases, all_bases]))
            + [prepared_sequence]
        )
    for item in all_possibilities:
        all_sequences.append(rewrite_codons_to_sequence(item))
    return all_sequences


def prepare_sequences(sequence):
    """Creates possibilities of sequence to be dividable by codons.
    
    Takes the sequence which len is not dividable by 3 and creates
    all the possibility sequences containing the target yet being
    able to be dividable by 3.

    Returns:
        List of sequences containing the target sequence
        and dividable by 3.
    """
    all_sequences = []
    all_bases = ["A", "C", "G", "U"]
    if len(sequence) % 3 == 1:
        all_possibilities = (
            list(product(*[[sequence], all_bases, all_bases]))
            + list(product(*[all_bases, [sequence], all_bases]))
            + list(product(*[all_bases, all_bases, [sequence]]))
        )
    else:
        all_possibilities = list(product(*[all_bases, [sequence]])) + list(
            product(*[[sequence], all_bases])
        )
    for item in all_possibilities:
        all_sequences.append(rewrite_codons_to_sequence(item))
    return all_sequences


def erase_not_shortest_sequences(good_sequences):
    """Returns all sequences which are the shortest"""
    optimal_lenght = 2147483646
    good_keys = list(good_sequences.keys())
    for sequence in good_keys:
        if len(sequence) < optimal_lenght:
            optimal_lenght = len(sequence)
    for sequence in good_keys:
        if len(sequence) > optimal_lenght:
            good_sequences.pop(sequence)
    return good_sequences
