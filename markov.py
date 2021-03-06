"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    opened_file = open(file_path).read()
    

    return opened_file

working_file = open_and_read_file('gettysburg.txt')
# print(working_file)


example_dict = {('a', 'fox?'): ['Would'],
 ('Sam', 'I'): ['am?'],
 ('could', 'you'): ['in', 'with', 'in', 'with'],
 ('you', 'with'): ['a', 'a'],
 ('box?', 'Would'): ['you'],
 ('ham?', 'Would'): ['you'],
 ('you', 'in'): ['a', 'a'],
 ('a', 'house?'): ['Would'],
 ('like', 'green'): ['eggs'],
 ('like', 'them,'): ['Sam'],
 ('and', 'ham?'): ['Would'],
 ('Would', 'you'): ['could', 'could', 'could', 'could', 'like', 'like'],
 ('you', 'could'): ['you', 'you', 'you', 'you'],
 ('a', 'mouse?'): ['Would'],
 ('them,', 'Sam'): ['I'],
 ('in', 'a'): ['house?', 'box?'],
 ('with', 'a'): ['mouse?', 'fox?'],
 ('house?', 'Would'): ['you'],
 ('a', 'box?'): ['Would'],
 ('green', 'eggs'): ['and'],
 ('you', 'like'): ['green', 'them,'],
 ('mouse?', 'Would'): ['you'],
 ('fox?', 'Would'): ['you'],
 ('eggs', 'and'): ['ham?']
}


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    word = text_string.split()
    
    for i in range(len(word) - 2):
        #test_chains = []
        key = (word[i], word[i + 1])
        value = [] #appending new words value list (see below)
        #test_list.append(word[i + 2])
    #for j in range(len(word) -2, -1):
    #     # edit to only loop over last two words in list
    #     #test_list = []
    #     #test_list.append(word[i + 2])
    #     chains[ word[j], word[j + 1] ] = (word[0])
        
        
        #if key in chains:
        #chains.has_key([ word[i], word[i + 1] ])
        if chains.get(key) is not None:
            chains[key].append(word[i + 2])  #add this word to existing list in dictionary
        else:
            value.append(word[i + 2])
            chains[ word[i], word[i + 1] ] = value #.append(word[i + 2])
        # value = value.append(word[i + 2])
            # if True:
                # value = value.append(word[i + 2])
            #chains[key] = value.append(word[i + 2])
            
        # each value in dict, "chains" should be a list
        # check if key in dict, if it is, append new word to value (that is a list) for key 

        # d[key] = d.get(key, 0) + 1
        #test_chains.append(chains[ word[i], word[i + 1] ])
        #print(test_list)
        # if chains[ word[i], word[i + 1] ] in test_list:
        #     print('it executes!')
            #test_list.append(word[i + 2])
        #     chains[]
    return(chains)
        

    # for j in range(len(word) -2, -1):
    #     # edit to only loop over last two words in list
    #     #test_list = []
    #     #test_list.append(word[i + 2])
    #     chains[ word[j], word[j + 1] ] = (word[0]) # value should be first word in list
    
        

# create empty dictionary
# take text input as a string, split that string into words
# iterate over list of words in range of length of list minus one
    # create key in dictionary for each pair of two words in list of words
    # assign value to key in dictionary that is equal to next word in list after pair
    # ?? make list as value and append words to list??



    # print(word)

        #print(chains)

    # print('*'* 10)
    #print(chains.keys())

test_function = make_chains(working_file)
print(test_function)

if test_function == example_dict:
    print('it matches')

import random
def make_text(chains):
    """Return text from chains."""

    link_words = []
    length = len(chains)
    #print(length)
    rand_num =  random.randint(0, length)
    # print(rand_num)

    rand_key = (random.choice(list(chains)))
    # link_words.append(str(rand_key))
    
    print(f'rand key = {rand_key}')

    #link_words.append(rand_key + rand_key+1)

    # link_words.append(str(chains[rand_key]))

    random_value = random.choice(chains[rand_key])
    print(f'rand value = {random_value}')
    link_words.append(random_value)

    (key_words, value_words) = rand_key
    link_words.append(key_words)
    link_words.append(value_words)
    print(f'link = {link_words}')
    # pick random key from dictionary
    # add tuple values of selected key to "link_words" list
    # look up value for key in dictionary
    # add random value from dictionary list to "link_words" list
    # use last two words of "link_words" list as new key
    # repeat!
    new_key = (link_words[-2], link_words[-1])
    print(f'new_key = {new_key}')
    
    if new_key in chains:
        link_chains = random.choice(chains[new_key])
        link_words.append(link_chains)
        print(f'link words = {link_words}')

    new_key = (link_words[-2], link_words[-1])
    print(f'new_key = {new_key}')
    
    if new_key in chains:
        link_chains = random.choice(chains[new_key])
        link_words.append(link_chains)
        print(f'link words = {link_words}')

    new_key = (link_words[-2], link_words[-1])
    print(f'new_key = {new_key}')
    
    if new_key in chains:
        link_chains = random.choice(chains[new_key])
        link_words.append(link_chains)
        print(f'link words = {link_words}')

    
    new_key = (link_words[-2], link_words[-1])
    print(f'new_key = {new_key}')
    
    if new_key in chains:
        link_chains = random.choice(chains[new_key])
        link_words.append(link_chains)
        print(f'link words = {link_words}')

    new_key = (link_words[-2], link_words[-1])
    print(f'new_key = {new_key}')
    
    if new_key in chains:
        link_chains = random.choice(chains[new_key])
        link_words.append(link_chains)
        print(f'link words = {link_words}')

    new_key = (link_words[-2], link_words[-1])
    print(f'new_key = {new_key}')

    if new_key in chains:
        link_chains = random.choice(chains[new_key])
        link_words.append(link_chains)
        print(f'link words = {link_words}')

    new_key = (link_words[-2], link_words[-1])
    print(f'new_key = {new_key}')

    if new_key in chains:
        link_chains = random.choice(chains[new_key])
        link_words.append(link_chains)
        print(f'link words = {link_words}')

    new_key = (link_words[-2], link_words[-1])
    print(f'new_key = {new_key}')

    if new_key in chains:
        link_chains = random.choice(chains[new_key])
        link_words.append(link_chains)
        print(f'link words = {link_words}')

    new_key = (link_words[-2], link_words[-1])
    print(f'new_key = {new_key}')
    
    if new_key in chains:
        link_chains = random.choice(chains[new_key])
        link_words.append(link_chains)
        print(f'link words = {link_words}')
    
    new_key = (link_words[-2], link_words[-1])
    print(f'new_key = {new_key}')
    
    if new_key in chains:
        link_chains = random.choice(chains[new_key])
        link_words.append(link_chains)
        print(f'link words = {link_words}')

    new_key = (link_words[-2], link_words[-1])
    print(f'new_key = {new_key}')

    if new_key in chains:
        link_chains = random.choice(chains[new_key])
        link_words.append(link_chains)
        print(f'link words = {link_words}')

    new_key = (link_words[-2], link_words[-1])
    print(f'new_key = {new_key}')

    if new_key in chains:
        link_chains = random.choice(chains[new_key])
        link_words.append(link_chains)
        print(f'link words = {link_words}')

    new_key = (link_words[-2], link_words[-1])
    print(f'new_key = {new_key}')

    if new_key in chains:
        link_chains = random.choice(chains[new_key])
        link_words.append(link_chains)
        print(f'link words = {link_words}')

    new_key = (link_words[-2], link_words[-1])
    print(f'new_key = {new_key}')

    if new_key in chains:
        link_chains = random.choice(chains[new_key])
        link_words.append(link_chains)
        print(f'link words = {link_words}')

    new_key = (link_words[-2], link_words[-1])
    print(f'new_key = {new_key}')

    if new_key in chains:
        link_chains = random.choice(chains[new_key])
        link_words.append(link_chains)
        print(f'link words = {link_words}')

    new_key = (link_words[-2], link_words[-1])
    print(f'new_key = {new_key}')

    if new_key in chains:
        link_chains = random.choice(chains[new_key])
        link_words.append(link_chains)
        print(f'link words = {link_words}')

    new_key = (link_words[-2], link_words[-1])
    print(f'new_key = {new_key}')

    def create_new_key(words_from_list):
        words_from_list = (link_words[-2], link_words[-1])
        if words_from_list in chains:
            link_chains = random.choice(chains[words_from_list])
            link_words.append(link_chains)
        return 

        #function above is going to iterate through new key and value variables, and
        #append into link_chains after every iteration
    

    return ' '.join(link_words)


input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
