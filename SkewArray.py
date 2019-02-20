# Input:  A String Genome
# Output: The skew array of Genome as a list.
def SkewArray(Genome):
    # your code here
    Skew = [0 for i in range(len(Genome)+1)]
    for i in range(len(Genome)):
        if Genome[i] == 'A' or Genome[i] == 'T':
            Skew[i+1] = Skew[i]
        elif Genome[i] == 'C':
            Skew[i+1] = Skew[i] - 1
        else:
            Skew[i+1] = Skew[i] + 1
            
    return Skew