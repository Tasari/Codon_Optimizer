from .Format_Codon_Bias import format_codon_bias
from .Maximize_CAI import maximize_CAI
from .tools import rewrite_sequence_to_aminoacids

def optimize(codon_bias, input_gene, output_gene):
    global final_sequence
    formatted_codon_bias = format_codon_bias(codon_bias)
    final_sequence = maximize_CAI(rewrite_sequence_to_aminoacids(input_gene), \
                                      formatted_codon_bias)

    output_gene.set_data(final_sequence)
                            