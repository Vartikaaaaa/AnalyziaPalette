def get_reverse_complement(sequence: str) -> str:
    complement = {"A": "T", "T": "A", "C": "G", "G": "C"}
    return ''.join(complement.get(base, base) for base in reversed(sequence))
