import pytest
from src.Backend.Format_Codon_Bias import format_codon_bias, create_formatted_codon_bias_from_sequence, set_rare_codons
from src.Backend.Codon import Codon
from src.Backend.CAI_calculation import calculate_CAI
from src.Backend.Maximize_CAI import maximize_CAI
from src.Backend.tools import *

initial_gene = '''
ATGAGGGGCATGAAGCTGCTGGGGGCGCTGCTGGCACTGGCGGCCCTACTGCAGGGGGCCGT
GTCCCTGAAGATCGCAGCCTTCAACATCCAGACATTTGGGGAGACCAAGATGTCCAATGCCACCC
TCGTCAGCTACATTGTGCAGATCCTGAGCCGCTATGACATCGCCCTGGTCCAGGAGGTCAGAGA
CAGCCACCTGACTGCCGTGGGGAAGCTGCTGGACAACCTCAATCAGGATGCACCAGACACCTAT
CACTACGTGGTCAGTGAGCCACTGGGACGGAACAGCTATAAGGAGCGCTACCTGTTCGTGTACA
GGCCTGACCAGGTGTCTGCGGTGGACAGCTACTACTACGATGATGGCTGCGAGCCCTGCGGGA
ACGACACCTTCAACCGAGAGCCAGCCATTGTCAGGTTCTTCTCCCGGTTCACAGAGGTCAGGGA
GTTTGCCATTGTTCCCCTGCATGCGGCCCCGGGGGACGCAGTAGCCGAGATCGACGCTCTCTAT
GACGTCTACCTGGATGTCCAAGAGAAATGGGGCTTGGAGGACGTCATGTTGATGGGCGACTTCA
ATGCGGGCTGCAGCTATGTGAGACCCTCCCAGTGGTCATCCATCCGCCTGTGGACAAGCCCCAC
CTTCCAGTGGCTGATCCCCGACAGCGCTGACACCACAGCTACACCCACGCACTGTGCCTATGACA
GGATCGTGGTTGCAGGGATGCTGCTCCGAGGCGCCGTTGTTCCCGACTCGGCTCTTCCCTTTAAC
TTCCAGGCTGCCTATGGCCTGAGTGACCAACTGGCCCAAGCCATCAGTGACCACTATCCAGTGG
AGGTGATGCTGAAGTGA
'''

initial_codon_bias_table = '''
UUU  8.2(    15)  UCU  2.2(     4)  UAU 11.5(    21)  UGU  3.3(     6)
UUC 31.1(    57)  UCC 11.5(    21)  UAC 16.9(    31)  UGC  9.8(    18)
UUA  0.5(     1)  UCA  2.2(     4)  UAA  0.5(     1)  UGA  2.2(     4)
UUG 11.5(    21)  UCG 13.6(    25)  UAG  0.0(     0)  UGG 15.3(    28)

CUU 16.9(    31)  CCU  2.2(     4)  CAU 15.3(    28)  CGU 10.4(    19)
CUC 25.6(    47)  CCC  9.8(    18)  CAC 18.0(    33)  CGC 21.8(    40)
CUA  2.2(     4)  CCA  7.1(    13)  CAA  7.1(    13)  CGA  5.5(    10)
CUG 26.2(    48)  CCG 28.4(    52)  CAG 21.3(    39)  CGG 24.5(    45)

AUU 10.9(    20)  ACU  3.8(     7)  AAU 10.9(    20)  AGU  4.4(     8)
AUC 31.1(    57)  ACC 25.1(    46)  AAC 17.5(    32)  AGC 10.4(    19)
AUA  2.7(     5)  ACA  6.0(    11)  AAA 13.6(    25)  AGA  4.4(     8)
AUG 27.3(    50)  ACG 25.6(    47)  AAG 35.5(    65)  AGG  4.9(     9)

GUU 11.5(    21)  GCU  9.3(    17)  GAU 20.2(    37)  GGU 14.7(    27)
GUC 42.6(    78)  GCC 46.9(    86)  GAC 30.6(    56)  GGC 46.4(    85)
GUA  0.5(     1)  GCA 15.3(    28)  GAA 32.2(    59)  GGA 12.0(    22)
GUG 22.9(    42)  GCG 37.6(    69)  GAG 31.6(    58)  GGG  9.3(    17)
'''

def test_set_rare_codons():
    formatted = set_rare_codons([Codon('AAA', 0.0, 0, 'H')])
    assert formatted[0].frequencyper1000 == 0.1

def test_formatting_codon_bias():
    formatted_codon_bias = format_codon_bias(initial_codon_bias_table)
    assert formatted_codon_bias[0].bases == 'UUU'
    assert formatted_codon_bias[1].frequencyper1000 == 2.2
    assert formatted_codon_bias[2].amount == 21

def test_formatting_sequence_to_codon_bias():
    formatted_codon_bias = create_formatted_codon_bias_from_sequence('CGACGGAGG')
    assert formatted_codon_bias[0].bases == 'CGA'
    assert formatted_codon_bias[1].amount == 0
    assert formatted_codon_bias[2].frequencyper1000 == 0.1

def test_CAI_calculation():
    formatted_codon_bias = format_codon_bias(initial_codon_bias_table)
    assert(calculate_CAI('UUCUUCUUC', formatted_codon_bias, alldata=0) == 1)
    assert(calculate_CAI('UUCUUCUUU', formatted_codon_bias, alldata=0) == 0.641)

def test_CAI_maximalization():
    formatted_codon_bias = format_codon_bias(initial_codon_bias_table)
    aminoacid_sequence = 'DADARAVE'
    sequence = maximize_CAI(aminoacid_sequence, formatted_codon_bias)
    assert(calculate_CAI(sequence, formatted_codon_bias, alldata=0) == 1)

def test_rewriting():
    assert(rewrite_sequence_to_protein('AUACUAGGC') == 'ILG')
    assert(rewrite_sequence_to_codons('AUACUAGGC') == ['AUA', 'CUA', 'GGC'])
    assert(rewrite_sequence_to_aminoacids('AUACUAGGC') == ['I', 'L', 'G'])
    assert(rewrite_codons_to_sequence(['AUA', 'CUA', 'GGC']) == 'AUACUAGGC')
    assert(rewrite_codons_to_protein(['AUA', 'CUA', 'GGC']) == 'ILG')
    assert(rewrite_codons_to_aminoacids(['AUA', 'CUA', 'GGC']) == ['I', 'L', 'G'])

def test_get_most_frequent_codons():
    assert(get_most_frequent_codons(format_codon_bias(initial_codon_bias_table))['P'].bases == 'CCG')
