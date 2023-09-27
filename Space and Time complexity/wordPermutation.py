def permutation(string,i=0):
    if i == len(string):   	 
        print("".join(string))
        
    for j in range(i,len(string)):
        words = [c for c in string]
        
        words[i],words[j] = words[j], words[i]
        
        permutation(words,i=i+1)
        
        
print(permutation("gowtham"))

"""The loop does indeed run for each character in the string, which is n times. Therefore, the time complexity of the loop is O(n).

The recursive function generates permutations of the string, and in the worst case, it generates all n! permutations. So, the recursive part contributes O(n!) to the overall time complexity.

So, the correct overall time complexity of the code is O(n * n!), not O(n * n * n!).

I appreciate your clarification, and I apologize for any confusion in my previous response. Thank you for pointing out the error."""