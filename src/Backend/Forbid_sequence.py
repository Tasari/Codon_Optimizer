import re 
from .tools import get_most_frequent_codons, rewrite_sequence_to_aminoacids

def forbid_sequences(sequences_list, input_gene, formatted_codon_bias_table):
    final_sequence = input_gene
    n=2
    if sequences_list == ['']:
        return final_sequence
    for sequence in sequences_list:
        while [found.start() for found in re.finditer(re.compile(sequence.replace('T', 'U')), final_sequence)] != []:
            last_sequences = [found.start() for found in re.finditer(re.compile(sequence.replace('T', 'U')), final_sequence)]
            final_sequence = forbid_sequence(sequence, final_sequence, formatted_codon_bias_table, n)
            if last_sequences == [found.start() for found in re.finditer(re.compile(sequence.replace('T', 'U')), final_sequence)]:
                n +=1
                if n !=8:
                    continue
                else:
                    print('Unsuccessfull')
                    return final_sequence 
            n=2
    return final_sequence




def forbid_sequence(sequence, input_gene, formatted_codon_bias_table, n=2):
    occurances = [found.start() for found in re.finditer(re.compile(sequence.replace('T', 'U')), input_gene)]
    if occurances == []:
        return input_gene
    lenght = len(sequence)
    alter = get_most_frequent_codons(formatted_codon_bias_table, n)
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
            modified_sequence += alter[aminoacid].bases
        final_sequence += input_gene[last:start] + modified_sequence
        last = start+lenght
    final_sequence += input_gene[last:]
    return final_sequence
