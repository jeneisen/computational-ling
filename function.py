def print_positions(word_list):
    for index,word in enumerate(word_list):
        print index, word


def print_table(dictionary):
    for key in sorted(dictionary):
        print key, dictionary[key]

def vocabulary(text):
    return sorted(set(text))

def diversity(text):
    prefix = text[:1000]
    return len(vocabulary(prefix))




def flatten(list_of_list):
    out=[]
    for x in list_of_list:
        for y in x:    
            out.append(y)
    return out



def flatten_table(diction):
    list_vals=[]
    for val in diction:
        list_vals.append(diction[val])
        print sorted(flatten(list_vals))

def file_words(text_file):
    words=[]
    for line in open(text_file):
        for word in line.split():
            words.append(word)
    print words


def ingwords(list_strings):
    ing_words=[]
    for word in list_strings:
        if "ing" in word:
            ing_words.append(word)
    return sorted(set(ing_words))

table = {}
def byfirst(list_of_strs):
    for word in list_of_strs:
        table[word[0]] = word
    return table



def likely(text_obj):
    vocabulary = set(text_obj)
    adjectives = []
    for word in vocabulary:
        if word[-2:] == "ly":
            adjectives.append(word.strip("ly"))
    return sorted(adjectives)
        
