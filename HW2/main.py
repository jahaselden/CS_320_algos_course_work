

import math  # optional and you can delete this line if not useful


def check_incorrect_input(words, wordlist):
    if words is None or wordlist is None:
        return True
    elif isinstance(words, tuple) and isinstance(wordlist, tuple):
        return False
    else:
        return True


def search_word_in_wordlist(key, tuple, low, high):
    mid = math.floor((low + high) / 2)
    if low > high:
        return True
    if key.lower() == tuple[mid].lower():  # word is in wordlist, don't add to new tuple
        return False
    elif key.lower() < tuple[mid].lower():
        return search_word_in_wordlist(key, tuple, low, mid - 1)
    else:
        return search_word_in_wordlist(key, tuple, mid + 1, high)


def new_words(words, wordlist):

    list_of_tuples = []
    
    if check_incorrect_input(words, wordlist):
        return None 
    else:
        for w in words: 
            if search_word_in_wordlist(w, wordlist, 0, len(wordlist) - 1):
                list_of_tuples.append(w)
        return tuple(list_of_tuples)            
