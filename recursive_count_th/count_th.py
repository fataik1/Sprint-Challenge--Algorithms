'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    #We will take in a word/phase abd it will return the maount of times `th` occurs
    #Parameters - word(str): a word, phrase, sentence that is a string.
    # returns the number of times that `th` occurs
    
    # if the length of the string is < 2 charactersm it won't contain `th`
    #want to return 0 if that is the case
    if len(word) < 2:
        return 0
    
    #TBC = first characters of the string are `th` so add one
    elif word[0:2] == 'th':
        return 1 + count_th(word[1:])
    #otherwise, recur starting at the next index over
    else:
        return count_th(word[1:])

word = 'this thing goes on past them why do they look mad?'
print(count_th(word))
