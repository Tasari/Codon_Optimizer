# Genetic optimizer #

Genetic optimizer is tool for gene optimalization

## Features ##

- CAI maximalization
- Harmonization and CG AT balancing
- Hidden codons avoiding
- Repeating base remove
- Avoiding sequence(Bit laggy)
- Including sequence

## TODO ##

- Speeding up the avoiding process
- Bugcatching
- Logs tab
- Tests

### Optional ###

- Enabling usage of sequences instead of codon bias table
- Bigger control for user
- Citations

## Installation ##

### Prerequisites ###

- Python 3.7

### Usage ###

- Unpack repository
- Run main.py using python
- Put codon bias table into Codon Bias Table entry (CTRL+V)
- Put starting gene into Input Gene (CTRL+V)
- Check options which you would like to use
- Click OPTIMIZE
- Copy the Output Sequence (CTRL+A, CTRL+C)

## Changelog ##

Version 1.0.0 (Recent):

- New:

    1. Working CAI maximalization
    2. Working Harmonization and CG balance
    3. Working Include Sequence
    4. Laggy but working Forbid sequence and similar functions

- Known Bugs:

    1. Slow Forbid Sequence
    2. Forbid Sequence destroys CG balance
    3. Codon Bias table with too many CDS's crashes the program
