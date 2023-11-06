def masterMind(solution,guess):
    frequency = {}
    hits = 0
    partial_hits = set()
    if len(solution)!=len(guess):
        return "Error"
    for i in range(len(solution)):
        if solution[i] == guess[i]:
            hits += 1
        else:
            if solution[i] not in frequency:
                frequency[solution[i]] = 1
            else:
                frequency[solution[i]] += 1
    for i in range(len(guess)):
        if guess[i] in frequency and solution[i] != guess[i]:
            partial_hits.add(guess[i])
    return hits,len(partial_hits)
    

print(masterMind(["B","R","G","Y"],["G","R","B","Y"]))