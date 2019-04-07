def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError('The sequences should have the same length.')

    paired_sequence = zip(strand_a, strand_b)
    return len([0 for a, b in paired_sequence if a != b])
