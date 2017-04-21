#Simple Fun #135: Missing Alphabets

# dictionary of letter:count
# store greatest = greatest count of letter
# missing_letter = greatest count - count
# add to list of missing letters
def missing_alphabets(s):
    import collections
    letters = collections.defaultdict(int)
    for letter in s:
        letters[letter] += 1
    greatest = max(letters.values())
    
    
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    for letter in alphabet:
        if not letter in letters:
            letters[letter] = greatest
        else:
            letters[letter] = greatest - letters[letter]
    
    
    missing = "".join(sorted(letter * count for letter, count in letters.items() if letters[letter] > 0))
    return missing


missing_alphabets('abcdefghijklmnopqrstuvwxyy')
