from .Format_Codon_Bias import format_codon_bias
from .Maximize_CAI import maximize_CAI
from .tools import rewrite_sequence_to_aminoacids
from .CAI_calculation import calculate_CAI
from .Calculate_CG import calculateCGs, create_codon_bias_supersequence
from .Forbid_sequence import forbid_sequences, add_forbid_sequences_to_all
from .Harmonize import  Harmonize
from .Include_sequence import include_sequence
from .remove_hidden_codons import add_hidden_codons_to_forbidden
from .Repetitive_bases_remover import add_repetitive_bases_to_forbidden


def optimize(codon_bias, input_gene, output_gene, checklist_board):
    formatted_codon_bias = format_codon_bias(codon_bias.all_data())
    final_sequence = input_gene.all_data().replace('T', 'U').replace('\n', '')
    all_forbidden_sequences = []
    if checklist_board.CAI_maximize_check.get():
        final_sequence = maximize_CAI(rewrite_sequence_to_aminoacids(final_sequence), \
                                      formatted_codon_bias)
    if checklist_board.Harmonization_check.get():
        final_sequence = Harmonize(final_sequence, formatted_codon_bias, 5)
    if checklist_board.Hidden_STOP_check.get():
        all_forbidden_sequences = add_hidden_codons_to_forbidden(all_forbidden_sequences, checklist_board.get_hidden())
    if checklist_board.Repeat_remove_check.get():
        all_forbidden_sequences = add_repetitive_bases_to_forbidden(all_forbidden_sequences)
    if checklist_board.Forbidden_sequences_check.get():
        all_forbidden_sequences = add_forbid_sequences_to_all(all_forbidden_sequences, checklist_board.get_forbidden())
    if all_forbidden_sequences != []:
        final_sequence = forbid_sequences(all_forbidden_sequences, final_sequence, formatted_codon_bias)
    if checklist_board.Favored_sequences_check.get():
        final_sequence = include_sequence(checklist_board.get_favored(), final_sequence)
    output_gene.set_data(final_sequence.replace('U', 'T'))
    calculate_CAI(input_gene, formatted_codon_bias)
    calculate_CAI(output_gene, formatted_codon_bias)
    input_gene.set_CGs(calculateCGs(input_gene.all_data()))
    output_gene.set_CGs(calculateCGs(output_gene.all_data()))
    codon_bias.set_CGs(calculateCGs(create_codon_bias_supersequence(formatted_codon_bias)))