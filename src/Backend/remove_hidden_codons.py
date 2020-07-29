def add_hidden_codons_to_forbidden(forbidden_list, codons_list):
    for codon in codons_list:
        if codon != '':
            forbidden_list += create_hidden_codons(codon)
    return forbidden_list

def create_hidden_codons(codon):
    all_hidden_possibilites = []
    bases = ['A', 'C', 'G', 'U']
    for base in bases:
        all_hidden_possibilites.append(codon[0]+base+codon[1]+codon[2])
        all_hidden_possibilites.append(codon[0]+codon[1]+base+codon[2])
    return all_hidden_possibilites
