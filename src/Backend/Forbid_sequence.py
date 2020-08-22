import re 
from .tools import get_most_frequent_codons, rewrite_sequence_to_aminoacids, find_sequence_in_gene, rewrite_codons_to_sequence
from itertools import product
from .CAI_calculation import calculate_CAI
from ..logs import errors, failed_forbidding

def check_if_sequences_in_forbidden(sequence, all_forbidden_sequences):
    for forbidden in all_forbidden_sequences:
        if find_sequence_in_gene(forbidden, sequence) != []:
            return 1
    return 0

def add_forbid_sequences_to_all(all_forbidden_sequences, new_forbidden):
    for sequence in new_forbidden:
        if sequence != '':
            all_forbidden_sequences.append(sequence)
    return all_forbidden_sequences

def get_sequence_from_occurance_places(input_gene, occurance, lenght):
    if occurance%3 == 0:
        start = occurance-3
    elif occurance%3 == 1:
        start = occurance-1-3
    else:
        start = occurance-2-3
    if start < 0:
        start=0
    end = start+lenght+3
    if end > len(input_gene):
        end = len(input_gene) 
    return (start, end)

def get_valid_sequence_lenght(sequence):
    lenght = len(sequence)
    if lenght%3 != 0:
        lenght += 1
        if lenght%3 != 0:
            lenght += 1
    return lenght

def get_codons_based_on_aminoacid(aminoacids, formatted_codon_bias_table):
    sequence = []
    for aminoacid in aminoacids:
        list_of_coding_codons = []
        for codon in formatted_codon_bias_table:
            if codon.aminoacid == aminoacid:
                list_of_coding_codons.append(codon.bases)
        sequence.append(list_of_coding_codons)
    return sequence

def change_sequence_to_eliminate_occurance(input_string, done_sequences, formatted_codon_bias_table, pre='',post=''):
    aminoacids = rewrite_sequence_to_aminoacids(input_string)
    possible_codons_list = get_codons_based_on_aminoacid(aminoacids, formatted_codon_bias_table)
    all_possibilities = [rewrite_codons_to_sequence(x) for x in product(*possible_codons_list)]
    good_possibilities = []
    for possibility in all_possibilities:
        if not check_if_sequences_in_forbidden(pre+possibility+post, done_sequences):
            good_possibilities.append(possibility)
    if not len(good_possibilities):
        return input_string, 1
    best = (0, '')
    for possibility in good_possibilities:
        calculated = (calculate_CAI(possibility, formatted_codon_bias_table, 0), possibility)
        if calculated[0] > best[0]:
            best = calculated
    return best[1], 0

def eliminate_occurances_of_sequence(final_sequence, done_sequences, lenght, formatted_codon_bias_table):
    sequence = done_sequences[-1]
    all_occurances_of_sequence = find_sequence_in_gene(sequence, final_sequence)
    begin = 0
    new_sequence = ''
    failed = 0
    for occurance in all_occurances_of_sequence:
        sequence_range = get_sequence_from_occurance_places(final_sequence, occurance, lenght)
        if begin > sequence_range[0]:
            begin = sequence_range[0]
            new_sequence = new_sequence[:begin] 
        new_sequence += final_sequence[begin:sequence_range[0]]
        to_append, failed = change_sequence_to_eliminate_occurance(final_sequence[sequence_range[0]:sequence_range[1]],\
                                                                 done_sequences, formatted_codon_bias_table, new_sequence[sequence_range[0]-2:sequence_range[0]], final_sequence[sequence_range[1]:sequence_range[1]+2])
        new_sequence += to_append
        begin = sequence_range[1]
        if failed and sequence.replace('U', 'T') not in failed_forbidding:
            failed_forbidding.append(sequence.replace('U', 'T'))
    new_sequence += final_sequence[begin:]
    if all_occurances_of_sequence != []:
        final_sequence = new_sequence
    if find_sequence_in_gene(sequence, final_sequence) != [] and not failed:
        return final_sequence, 1
    return final_sequence, 0

def forbid_sequences(all_forbidden_sequences, input_string, formatted_codon_bias_table):
    final_sequence = input_string
    still_found=0
    if all_forbidden_sequences != []:
        all_forbidden_sequences = list(dict.fromkeys(sorted(all_forbidden_sequences, key=len)))
        still_found=1
        for number, sequence in enumerate(all_forbidden_sequences):
            all_forbidden_sequences[number] = sequence.replace('T', 'U')
    while still_found:
        done_sequences = [] 
        for sequence in all_forbidden_sequences:
            lenght = get_valid_sequence_lenght(all_forbidden_sequences[len(all_forbidden_sequences)-1])
            done_sequences.append(sequence)
            final_sequence, still_found = eliminate_occurances_of_sequence(final_sequence, done_sequences, lenght, formatted_codon_bias_table)
    errors.append("Failed to eliminate sequeces: {}".format(failed_forbidding))
    return final_sequence