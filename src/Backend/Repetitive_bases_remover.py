def add_repetitive_bases_to_forbidden(all_forbidden_sequences, amount=5):
    """Adds all repeating bases into forbidden.

    Creates sequences of repeating bases, lenght is defined
    by amount argument.

    Args:
        all_forbidden_sequences: List of all forbidden sequences.
        amount: Lenght of repeating bases to be removed.

    Returns:
        Forbidden sequences with added repetitive bases.
    """
    bases = ["A", "C", "G", "T"]
    for base in bases:
        all_forbidden_sequences.append(base * amount)
    return all_forbidden_sequences
