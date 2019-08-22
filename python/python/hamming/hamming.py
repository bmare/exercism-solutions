def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands are not the same length.")
    zipped=zip(strand_a, strand_b)
    difference = [(nuc_a, nuc_b) for nuc_a, nuc_b in zipped if nuc_a != nuc_b]
    return len(difference)
