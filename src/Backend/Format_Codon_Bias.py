from .Codon import Codon
from .data import codon_to_aminoacid
from .tools import rewrite_sequence_to_codons, rewrite_to_rna
from ..logs import errors


def format_codon_bias(codon_bias_table):
    codons = []
    actual_codon = {"bases": "", "frequencyper1000": "", "amount": "", "mode": "freq"}
    for char in codon_bias_table:
        if char in ["A", "C", "G", "U"]:
            actual_codon["bases"] += char
        elif (
            char in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]
            and actual_codon["mode"] == "freq"
        ):
            actual_codon["frequencyper1000"] += char
        elif char == "(":
            actual_codon["mode"] = "amount"
        elif (
            char in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
            and actual_codon["mode"] == "amount"
        ):
            actual_codon["amount"] += char
        elif char == ")":
            codons.append(
                Codon(
                    actual_codon["bases"],
                    float(actual_codon["frequencyper1000"]),
                    int(actual_codon["amount"]),
                    codon_to_aminoacid[actual_codon["bases"]],
                )
            )
            actual_codon = {
                "bases": "",
                "frequencyper1000": "",
                "amount": "",
                "mode": "freq",
            }
    codons = set_rare_codons(codons)
    return codons


def set_rare_codons(formatted_codons, minimal_frequency=0.1):
    for codon in formatted_codons:
        if codon.frequencyper1000 < minimal_frequency:
            codon.frequencyper1000 = minimal_frequency
    return formatted_codons


def create_formatted_codon_bias_from_sequence(sequence):
    codons = []
    sequence = change_sequence_to_use_only_bases_letters(sequence)
    codon_counts = count_codons(sequence)
    for key, value in codon_counts.items():
        codon_frequency = round(
            float(
                value * (len(rewrite_sequence_to_codons(sequence)) / 1000)
            ),
            1,
        )
        codons.append(Codon(key, codon_frequency, value, codon_to_aminoacid[key]))
    codons = set_rare_codons(codons)
    return codons


def change_sequence_to_use_only_bases_letters(sequence):
    whitelist = ["A", "C", "G", "U"]
    whitelisted_sequence = "".join(
        [char for char in rewrite_to_rna(sequence) if char in whitelist]
    )
    try:
        assert len(whitelisted_sequence) % 3 == 0
    except AssertionError:
        errors.append("Representative sequences are not dividable by 3")
        raise Exception
    return whitelisted_sequence


def count_codons(sequence):
    codon_counts = {}
    for key in codon_to_aminoacid.keys():
        codon_counts[key] = 0
    for codon in rewrite_sequence_to_codons(sequence):
        codon_counts[codon] += 1
    return codon_counts

