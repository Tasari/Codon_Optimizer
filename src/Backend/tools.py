from .data import codon_to_aminoacid
def rewrite_sequence_to_protein(sequence):
    return rewrite_codons_to_protein(rewrite_sequence_to_codons(sequence))

def rewrite_sequence_to_codons(sequence):
    codons=[]
    base=0
    for i in range(int(len(sequence)/3)):
        codons.append(sequence[base]+sequence[base+1]+sequence[base+2])
        base += 3
    return codons
    
def rewrite_sequence_to_aminoacids(sequence):
    return rewrite_codons_to_aminoacids(rewrite_sequence_to_codons(sequence))

def rewrite_codons_to_sequence(codons):
    sequence = ''
    for codon in codons:
        sequence += codon
    return sequence

def rewrite_codons_to_protein(codons):
    protein = ''
    for codon in codons:
        protein += codon_to_aminoacid[codon]
    return protein

def rewrite_codons_to_aminoacids(codons):
    aminoacids=[]
    for codon in codons:
        aminoacids.append(codon_to_aminoacid[codon])
    return aminoacids

