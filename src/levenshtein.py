# min edit distance or cost to convert seq1 into seq2
def levenshtein(seq1 : str, seq2 : str) -> int:
    
    cache = [[float("inf")] * (len(seq2) + 1) for i in range(len(seq1) + 1)] # DP table
    
    for j in range(len(seq2) + 1):
        cache[len(seq1)][j] = len(seq2) - j
    
    for i in range(len(seq1) + 1):
        cache[i][len(seq2)] = len(seq1) - i
    
    for i in range(len(seq1) - 1, -1, -1):
        for j in range(len(seq2) - 1, -1, -1):
            if seq1[i] == seq2[j]:
                cache[i][j] = cache[i+1][j+1] 
            else:
                cache[i][j] = 1 + min(cache[i][j+1],cache[i+1][j],cache[i+1][j+1])
                
    return cache[0][0]
  
            
            
print(levenshtein("horse","ros"))