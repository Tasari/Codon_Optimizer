def add_repetitive_bases_to_forbidden(all_forbidden_sequences, amount=5):
    bases = ["A", "C", "G", "T"]
    for base in bases:
        all_forbidden_sequences.append(base * amount)
    return all_forbidden_sequences
