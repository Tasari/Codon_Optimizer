def add_hidden_codons_to_forbidden(forbidden_list, codons_list):
    for codon in codons_list:
        if codon != '':
            forbidden_list += create_hidden_codons(codon)
    return forbidden_list

def create_hidden_codons(codon_string):
    all_hidden_possibilites = []
    bases = ['A', 'C', 'G', 'T']
    for base in bases:
        all_hidden_possibilites.append(codon_string[0]+base+codon_string[1]+codon_string[2])
        all_hidden_possibilites.append(codon_string[0]+codon_string[1]+base+codon_string[2])
    return list(set(all_hidden_possibilites))
