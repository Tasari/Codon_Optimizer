from .Calculate_CG import calculateCGs
from .tools import (
    get_most_frequent_codons,
    rewrite_sequence_to_codons,
    create_codon_bias_supersequence,
)
import re


def Harmonize(sequence, formatted_codons, spread=5):
    """Eliminates nth codon reapeat to make it easier to fold protein.

    Changes the sequence to use secondary codon after some
    repeats of the same codon for aminoacid. It makes it
    easier to correctly fold the protein. 
    
    Example:
        Harmonize("AACAACAAC", codons, 3): "AACAACAAU"
        where codon AAC and AAU both code N aminoacid 
        and AAC is more frequent one.

    Args:
        sequence: 
            Sequence to be harmonized.
        formatted_codons: 
            List of all Codons.
        spread: 
            How frequent the change is, 
            lower spread means more replacecs.

    Returns:
        Harmonized sequence string.
    """
    for codon in get_most_frequent_codons(formatted_codons).values():
        actual_cgcontent = calculateCGs(sequence)
        prioritized_codon = get_best_codon_with_optimal_score(
            formatted_codons, actual_cgcontent, codon.aminoacid
        )
        sequence = replace_nth_codon(
            sequence, codon.bases, prioritized_codon.bases, spread
        )
    return sequence


def get_best_codon_with_optimal_score(
    formatted_codons, actual_cgcontent, aminoacid
):
    """Gets secondary codon to replace the primary one in sequence.

    Gets needed cgs on each place, and scores each codon coding the
    same aminoacid, then takes the highest score codons 
    and selects one with highest frequency.

    Args: 
        formatted_codons: List of formatted Codons.
        actual_cgcontent: CGcontent of actual sequence.
        aminoacid: Aminoacid we want to keep.

    Returns:
        Codon object with highest score and frequency.
    """
    all_aa_codons = {}
    supersequence = create_codon_bias_supersequence(formatted_codons)
    target_cgcontent = calculateCGs(supersequence)
    cg1, cg2, cg3 = define_needed_cgs(actual_cgcontent, target_cgcontent)
    for codon in formatted_codons:
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
    """Defines if codons on each place shoud be increased or decreased.
    
    Compares the actual CG content with target CG content 
    leaving window of 2, returns tuple of 3 number, each
    telling about the corresponding place, 1 for 
    place where CG content should be increased, 0
    if it should be kept, or -1 if it should be decreased.

    Args:
        Actual_cgcontent: CG content of sequence
        Target_cgcontent: CG content of Codons objects list
    """
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
    """Scores codon based on needed CGs on each place.

    Takes each letter of the codon and changes it's score
    based on passed cg1, cg2 and cg3. Also takes frequency
    of codon into account, so rare codons are not overused.

    Args:
        codon: Codon object we want to score.
        cg1, cg2, cg3: Int indicators of scoring the codons.

    Returns:
        Score integer.
    """
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
    """Replaces each nth old codon of sequence with new one"""
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
