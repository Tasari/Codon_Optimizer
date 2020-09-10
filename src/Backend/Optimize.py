from .Format_Codon_Bias import format_codon_bias, create_formatted_codon_bias_from_sequence
from .Maximize_CAI import maximize_CAI
from .tools import rewrite_sequence_to_aminoacids, rewrite_to_rna
from .CAI_calculation import calculate_CAI
from .Calculate_CG import calculateCGs
from .Forbid_sequence import forbid_sequences, add_forbid_sequences_to_all
from .Harmonize import  Harmonize
from .Include_sequence import include_sequence
from .remove_hidden_codons import add_hidden_codons_to_forbidden
from .Repetitive_bases_remover import add_repetitive_bases_to_forbidden
from .tools import create_codon_bias_supersequence
from ..logs import errors, failed_forbidding

def create_checklist_board_list(checklist_board):
    checklist_board_list = []
    checklist_board_list.append(checklist_board.CAI_maximize_check.get())
    checklist_board_list.append(checklist_board.Harmonization_check.get())
    checklist_board_list.append((checklist_board.Hidden_STOP_check.get(), \
                                 checklist_board.get_hidden()))
    checklist_board_list.append(checklist_board.Repeat_remove_check.get())
    checklist_board_list.append((checklist_board.Forbidden_sequences_check.get(), \
                                 checklist_board.get_forbidden()))
    checklist_board_list.append((checklist_board.Favored_sequences_check.get(), \
                                 checklist_board.get_favored()))
    return checklist_board_list

def front_optimize(codon_bias_entry, input_gene_entry, output_gene_entry, checklist_board, logs):
    try:
        if not codon_bias_entry.var.get():
            codon_bias_entry.check_table_valid()
            formatted_codon_bias = format_codon_bias(codon_bias_entry.all_data())
        else:
            formatted_codon_bias = create_formatted_codon_bias_from_sequence(codon_bias_entry.all_data())
        input_gene_entry.check_if_text_is_gene()
        input_gene_text = rewrite_to_rna(input_gene_entry.all_data())
        checklist_board_list = create_checklist_board_list(checklist_board)
        output_gene_entry.set_data(optimize(formatted_codon_bias, input_gene_text, checklist_board_list))
        output_gene_text = rewrite_to_rna(output_gene_entry.all_data())
        input_gene_entry.set_CAI(calculate_CAI(input_gene_text, formatted_codon_bias))
        output_gene_entry.set_CAI(calculate_CAI(output_gene_text, formatted_codon_bias))
        input_gene_entry.set_CGs(calculateCGs(input_gene_text))
        output_gene_entry.set_CGs(calculateCGs(output_gene_text))
        supersequence = create_codon_bias_supersequence(formatted_codon_bias)
        codon_bias_entry.set_CGs(calculateCGs(supersequence))
    except:
        pass
    finally:
        logs.add_errors(errors)
        errors.clear()
        failed_forbidding.clear()

def optimize(formatted_codon_bias, input_gene_text, checklist_board_list):
    input_gene_text = rewrite_to_rna(input_gene_text)
    try:
        try:
            assert(len(input_gene_text) % 3 == 0)
        except AssertionError:
            errors.append("Input Sequence is not dividable by 3")
            raise Exception
        try:
            assert(len(formatted_codon_bias) == 64)
        except AssertionError:
            errors.append("Not enough codons in table")
            raise Exception
        all_forbidden_sequences = []
        if checklist_board_list[0]:
            final_sequence = maximize_CAI(rewrite_sequence_to_aminoacids(input_gene_text), \
                                        formatted_codon_bias)
        if checklist_board_list[1]:
            final_sequence = Harmonize(final_sequence, formatted_codon_bias, 5)
        if checklist_board_list[2][0]:
            all_forbidden_sequences = add_hidden_codons_to_forbidden(all_forbidden_sequences, checklist_board_list[2][1])
        if checklist_board_list[3]:
            all_forbidden_sequences = add_repetitive_bases_to_forbidden(all_forbidden_sequences)
        if checklist_board_list[4][0]:
            all_forbidden_sequences = add_forbid_sequences_to_all(all_forbidden_sequences, checklist_board_list[4][1])
        if all_forbidden_sequences != []:
            final_sequence = forbid_sequences(all_forbidden_sequences, final_sequence, formatted_codon_bias)
        if checklist_board_list[5][0]:
            final_sequence = include_sequence(checklist_board_list[5][1], final_sequence, formatted_codon_bias)
    except:
        pass
    return final_sequence.replace('U', 'T')
