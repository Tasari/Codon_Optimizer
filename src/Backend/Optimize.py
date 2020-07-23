from .Format_Codon_Bias import format_codon_bias
from .Maximize_CAI import maximize_CAI
from .tools import rewrite_sequence_to_aminoacids
from .CAI_calculation import calculate_CAI
from .Calculate_CG import calculateCGs, create_codon_bias_supersequence
from .Forbid_sequence import forbid_sequence
def optimize(codon_bias, input_gene, output_gene, checklist_board):
    formatted_codon_bias = format_codon_bias(codon_bias.all_data())
    final_sequence = input_gene.all_data().replace('T', 'U').replace('\n', '')
    if checklist_board.CAI_maximize_check.get():
        final_sequence = maximize_CAI(rewrite_sequence_to_aminoacids(final_sequence), \
                                      formatted_codon_bias)
    if checklist_board.Forbidden_sequences_check.get():
        final_sequence = forbid_sequence(checklist_board.get_forbidden(), final_sequence, formatted_codon_bias)
    output_gene.set_data(final_sequence.replace('U', 'T'))
    calculate_CAI(input_gene, formatted_codon_bias)
    calculate_CAI(output_gene, formatted_codon_bias)
    input_gene.set_CGs(calculateCGs(input_gene.all_data()))
    output_gene.set_CGs(calculateCGs(output_gene.all_data()))
    codon_bias.set_CGs(calculateCGs(create_codon_bias_supersequence(formatted_codon_bias)))