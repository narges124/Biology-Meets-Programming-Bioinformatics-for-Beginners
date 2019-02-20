def Complement(Pattern):
    out = ""
    for test in Pattern:
        if test == 'T':
            out = out + 'A'
        if test == 'A':
            out = out + 'T'
        if test == 'C':
            out = out + 'G'
        if test == 'G':
            out = out + 'C'
    return out