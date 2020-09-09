# Genetic optimizer #

Genetic optimizer is tool for gene optimalization

## Features ##

- CAI maximalization
- Harmonization and CG AT balancing
- Hidden codons avoiding
- Repeating base remove
- Avoiding sequence(Can be slow with bigger sequences)
- Including sequence

## TODO ##

- Bugcatching
- Tests
- Refactoring

### Optional ###

- Enabling usage of sequences instead of codon bias table
- Bigger control for user
- Citations

## Installation ##

- Unpack repository
- Run main.py using python

### Prerequisites ###

- Python 3.7

## Usage ##

- Put codon bias table into Codon Bias Table entry (CTRL+V)
- Put starting gene into Input Gene (CTRL+V)
- Check options which you would like to use
- Click OPTIMIZE
- Copy the Output Sequence (CTRL+A, CTRL+C)

### Detailed function info ###

- CAI maximalization - Maximizes the CAI of sequence
- Harmonization and CG balance - Balancing CG while harmonizing the sequence (Planning user set spread)
- Erase hidden codons - Tries to remove given hidden codons, multiple codons are set using ", ", e.g. "UUG, TTC"
- Remove repeating bases - Tries to remove sequences like "CCCCC" (Planning user set lenght of sequence)
- Forbid sequence - Tries to avoid given sequences, e.g. "GAAG, CAAAACTAG"
- Include sequence - Tries to put given sequence somewhere into output, supports only 1 sequence at once(Planning multiple sequences)

## Changelog ##

Version 1.2.2:

- Updated:
    1. Repaired include sequence which didn't respect aminoacid sequences
- Known Bugs:
    1. Forbid sequence is not taking CG balance into account

Version 1.2.1:

- Updated:
    1. Eliminated bug with CAI calculation using representative sequence
- Known Bugs:
    1. Forbid sequence is not taking CG balance into account

Version 1.2.0:

- New:
    1. Enabled using sequences instead of table

- Known Bugs:
    1. Forbid sequence is not taking CG balance into account

Version 1.1.1:

- Updated:
    1. Eliminated too big codon bias table problem
    2. Allowed empty arguments in functions without errors, function is omitted
    3. Dealt with basic bad input errors, informing user via logs
    4. Bugfixed error showing eliminated sequences are not eliminated
    5. Bugfixed not working import

- Known Bugs:
    1. Forbid sequence is not taking CG balance into account

Version 1.1.0:

- New:

    1. Logs window (Shows erase errors)
    2. Quite fast forbid sequence

- Updated:

    1. Remade forbid sequence to be faster

- Known Bugs:

    1. Forbid Sequence destroys CG balance
    2. Codon Bias table with too many CDS's crashes the program
    3. Enabling some functions and passing empty arguments crashes the optimizing without logs error

Version 1.0.0:

- New:

    1. Working CAI maximalization
    2. Working Harmonization and CG balance
    3. Working Include Sequence
    4. Laggy but working Forbid sequence and similar functions

- Known Bugs:

    1. Slow Forbid Sequence
    2. Forbid Sequence destroys CG balance
    3. Codon Bias table with too many CDS's crashes the program
