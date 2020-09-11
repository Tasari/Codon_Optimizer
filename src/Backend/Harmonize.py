from .Calculate_CG import calculateCGs
from .tools import (
    get_most_frequent_codons,
    rewrite_sequence_to_codons,
    create_codon_bias_supersequence,
)
import re


def Harmonize(sequence, formatted_codon_bias, spread=5):
    supersequence = create_codon_bias_supersequence(formatted_codon_bias)
    target_cgcontent = calculateCGs(supersequence)
    for codon in get_most_frequent_codons(formatted_codon_bias).values():
        actual_cgcontent = calculateCGs(sequence)
        prioritized_codon = get_best_codon_with_optimal_score(
            formatted_codon_bias, actual_cgcontent, target_cgcontent, codon.aminoacid
        )
        sequence = replace_nth_codon(
            sequence, codon.bases, prioritized_codon.bases, spread
        )
    return sequence


def get_best_codon_with_optimal_score(
    formatted_codon_bias, actual_cgcontent, target_cgcontent, aminoacid
):
    all_aa_codons = {}
    cg1, cg2, cg3 = define_needed_cgs(actual_cgcontent, target_cgcontent)
    for codon in formatted_codon_bias:
        if codon.aminoacid == aminoacid:
            try:
                all_aa_codons[score(codon, cg1, cg2, cg3)].append(codon)
            except:
                all_aa_codons[score(codon, cg1, cg2, cg3)] = []
                all_aa_codons[score(codon, cg1, cg2, cg3)].append(codon)
        best = -1
    for codon in all_aa_codons[max(all_aa_codons.keys())]:
        if codon.frequencyper1000 > best:
            best = codon.frequencyper1000
            best_codon = codon
    return best_codon


def define_needed_cgs(actual_cgcontent, target_cgcontent):
    cg1, cg2, cg3 = 1, 1, 1
    if target_cgcontent[1] - 2 < actual_cgcontent[1] < target_cgcontent[1] + 2:
        cg1 = 0
    elif actual_cgcontent[1] > target_cgcontent[1] + 2:
        cg1 = -1
    if target_cgcontent[2] - 2 < actual_cgcontent[2] < target_cgcontent[2] + 2:
        cg2 = 0
    elif actual_cgcontent[2] > target_cgcontent[2]:
        cg2 = -1
    if target_cgcontent[3] - 2 < actual_cgcontent[3] < target_cgcontent[3] + 2:
        cg3 = 0
    elif actual_cgcontent[3] > target_cgcontent[3] + 2:
        cg3 = -1
    return (cg1, cg2, cg3)


def score(codon, cg1, cg2, cg3):
    score = 0
    if (codon.bases[0] == "G" or codon.bases[0] == "C") and cg1 == 1:
        score += 1
    elif (codon.bases[0] == "G" or codon.bases[0] == "C") and cg1 == 0:
        pass
    elif (codon.bases[0] == "G" or codon.bases[0] == "C") and cg1 == -1:
        score -= 1
    if (codon.bases[1] == "G" or codon.bases[1] == "C") and cg2 == 1:
        score += 1
    elif (codon.bases[1] == "G" or codon.bases[1] == "C") and cg2 == 0:
        pass
    elif (codon.bases[1] == "G" or codon.bases[1] == "C") and cg2 == -1:
        score -= 1
    if (codon.bases[2] == "G" or codon.bases[2] == "C") and cg3 == 1:
        score += 1
    elif (codon.bases[2] == "G" or codon.bases[2] == "C") and cg3 == 0:
        pass
    elif (codon.bases[2] == "G" or codon.bases[2] == "C") and cg3 == -1:
        score -= 1
    if codon.frequencyper1000 < 10:
        score -= 1
    return score


def replace_nth_codon(sequence, old, new, n):
    final_string = ""
    counter = 0
    codons = rewrite_sequence_to_codons(sequence)
    for codon in codons:
        if codon == old:
            counter += 1
            if counter == n:
                final_string += new
                counter = 0
            else:
                final_string += old
        else:
            final_string += codon
    return final_string
