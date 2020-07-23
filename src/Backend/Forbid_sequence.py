import re 
from .tools import get_second_most_frequent_codons, rewrite_sequence_to_aminoacids

def forbid_sequence(sequence, input_gene, formatted_codon_bias_table):
    occurances = [found.start() for found in re.finditer(re.compile(sequence.replace('T', 'U')), input_gene)]
    lenght = len(sequence)
    second = get_second_most_frequent_codons(formatted_codon_bias_table)
    final_sequence = ''
    last = 0
    if lenght%3 != 0:
        lenght += 1
        if lenght%3 != 0:
            lenght += 1
    for occurance in occurances:
        if occurance%3 == 0:
            start = occurance
            to_modify = input_gene[occurance:occurance+lenght]
        elif occurance%3 == 1:
            start = occurance-1
            to_modify = input_gene[occurance-1:occurance-1+lenght]
        else:
            start = occurance-2
            to_modify = input_gene[occurance-2:occurance-2+lenght]
        modified_sequence = ''
        for aminoacid in rewrite_sequence_to_aminoacids(to_modify):
            modified_sequence += second[aminoacid].bases
        final_sequence += input_gene[last:start] + modified_sequence
        last = start+lenght
    final_sequence += input_gene[last:]
    if occurances == []:
        return input_gene
    return final_sequence
