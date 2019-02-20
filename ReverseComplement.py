def ReverseComplement(Pattern):   
    Pattern = Reverse(Pattern)
    Pattern = Complement(Pattern)
    return Pattern

# Copy your Reverse() function here.
def Reverse(Pattern):
    # your code here
    out = ""
    for test in Pattern:
        out = test + out
    return out

# Copy your Complement() function here.
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