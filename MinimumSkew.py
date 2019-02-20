# Input:  A DNA string Genome
# Output: A list containing all integers i minimizing Skew(Prefix_i(Text)) over all values of i (from 0 to |Genome|)
def MinimumSkew(Genome):
    positions = [] # output variable
    Skew = SkewArray(Genome)
    m = min(Skew)
    #positions = Skew.index(m)
    for s in range(len(Skew)):
        if Skew[s] == m:
            positions.append(s)
    return positions

# Input:  A String Genome
# Output: SkewArray(Genome)
# HINT:   This code should be taken from the last Code Challenge.
def SkewArray(Genome):
    Skew = [0 for i in range(len(Genome)+1)]
    for i in range(len(Genome)):
        if Genome[i] == 'A' or Genome[i] == 'T':
            Skew[i+1] = Skew[i]
        elif Genome[i] == 'C':
            Skew[i+1] = Skew[i] - 1
        else:
            Skew[i+1] = Skew[i] + 1
            
    return Skew