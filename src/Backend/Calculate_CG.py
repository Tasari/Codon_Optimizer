def calculateCGs(sequence):
    sequence=sequence.replace('\n', '').replace(' ', '')
    cgtotal = 0
    cg1 = 0
    cg2 = 0
    cg3 = 0
    counter = 0
    totalall=len(sequence)
    for letter in sequence:
        if letter == 'C' or letter == 'G':
            if counter == 0:
                cg1+=1
                counter+=1
            elif counter == 1:
                cg2+=1
                counter+=1
            elif counter == 2:
                cg3+=1
                counter=0
            cgtotal+=1
        else:
            if counter == 2:
                counter = 0
            else:
                counter +=1
    return [cgtotal/totalall*100, cg1/(totalall/3)*100, cg2/(totalall/3)*100, cg3/(totalall/3)*100] 

def create_codon_bias_supersequence(formatted_codon_bias_table):
    superstring = ''
    for codon in formatted_codon_bias_table:
        superstring += codon.bases*codon.amount
    print(superstring)
    return superstring