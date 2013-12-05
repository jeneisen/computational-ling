#PART1

#1.
words = ["cat", "dog", "ali", "fido", "eisenberg", "bob", "zaney"]
sorted(words)
['ali', 'bob', 'cat', 'dog', 'eisenberg', 'fido', 'zaney']

#2. list containing the first five tokens of text1.
text1[0:5]
['[', 'Moby', 'Dick', 'by', 'Herman']

#3. If n is a number, turn it into a string.
str(3)
'3'

#4. . If words is a list of strings, replace the word at position i with 
the new
#word w. (You may assume that i is less than the length of words.)
words[i] = "w"
#assuming i is an actual integer less than length of words and w is a 
string

#5. Get the number of elements in the set s.
len(s)

#6. . Determine whether the element x is present in the set s.
x in s
#assumes x is predefined, otherwise would return a NameError
#returns True or False

# 7. Create an empty set.
set([])

#8. Associate the key k with the value v in the dict d
d= {}
d["k"] = "v" 
# d returns {'k': 'v'}
#assuming k and v should be strings

#9. Determine whether the word w is present (as key) in the dict d.
d["w"]
#returns KeyError if False otherwise returns value for the key
#or you can do
"w" in d
#returns False

#10.Determine whether the word w is absent from the dict d.
"w" not in d
#returns True

#11. Determine how many entries (keys) there are in the dict d.
len(d.keys()) 

#12. Create a dict that associates "foo" with value 6 and "bar" wth value 
42.
dictionary = {"foo":6, "bar":42}

#13. If s is a string (e.g., "this is a test"), get a list of strings 
representing
#the individual whitespace-separated tokens of s (e.g., ["this", "is",
#"a", "test"]).
s = "this is a test"
s.split()
#returns ['this', 'is', 'a', 'test']

#14. Get the last five words of Moby Dick. Assume that you have already 
done
#import nltk.book. Do not assume that you have already done from
#nltk.book import *, nor should your answer involve importing text1.
#(I.e., part of the question is how you can refer to text1 without 
actually
#importing it into your working space.)
text1 = nltk.book.text1
text1[-5:]
# returns ['only', 'found', 'another', 'orphan', '.']


#15. If words is a list of words, turn it into an NLTK text object. 
(Assume
#that you have already done import nltk

#16. If morphs is a list of strings (e.g., ['bash', 'ful', 'ly']), produce 
a
#single string in which they are all run together (e.g., 'bashfully'). 
Your
#expression should work no matter how many strings there are in morphs.
"".join(morphs)
#returns "bashfully"

#17. If phone is a string representing a phone number (e.g., 
'123-456-7890'),
#turn it into a list containing the parts between the hyphens (e.g., 
['123',
#'456', '7890'])
phone = "123-456-789"
phone.split("-")
['123', '456', '789']

#PART 2

#18.
#a)
def print_words(word_list):
  for word in word_list:
    print word
  
b) print_words(['another', 'test'])
#prints another and test on two separate lines
another
test

#19. Define a function called print_positions that takes a list and prints 
each
#element preceded by its position.

#a)
def print_positions(word_list):
        for index,word in enumerate(word_list):
                print index, word

#b)
print_positions(['a', 'b'])
0 a
1 b

#20. Define a function called print_table that prints each key in a dict, 
followed by its value. 
#It should print the keys in alphabetic order
#a)
def print_table(dictionary):
        for key in sorted(dictionary):      
                print key, dictionary[key]  
 
#b)
print_table({'this':'is', 'a':'test', 'foo':'bar'})
a test
foo bar
this is
 
#21. Define the function diversity from the end of Handout 4. (The 
diversity
#of a text is defined to be the number of types in the first 1000 words of
#the text.)
 
def vocabulary(text):
        return sorted(set(text))
 
def diversity(text):
        prefix = text[:1000]
        return len(vocabulary(prefix))
diversity(text1)
#prints 461
 
texts = [text1, text2, text3, text4, text5, text6, text7, text8, text9]
for book in texts:
        print  book.name, " : " + str(diversity(book))
        
Moby Dick by Herman Melville 1851  : 461
Sense and Sensibility by Jane Austen 1811  : 349
The Book of Genesis  : 187
Inaugural Address Corpus  : 452
Chat Corpus  : 407
Monty Python and the Holy Grail  : 285
Wall Street Journal  : 465
Personals Corpus  : 403
The Man Who Was Thursday by G . K . Chesterton 1908  : 456


#22. Define a function called flatten that takes a list of lists and 
returns a
#single list containing all the elements of the original lists.
#a)
         
def flatten(list_of_list):
        out = [] 
        for x in list_of_list:
                for y in x:
                        out.append(y)  
                        return out  
#b)
[4, 2, 3, 2, 5, 1]

#23. Dene a function called flatten_table that takes a dict containing 
values
#that are lists, and returns a single list containing all the values. 
This time,
#the list you return should be sorted.
#a)
def flatten_table(diction):
        list_vals=[]
        for val in diction:
                list_vals.append(diction[val])
                print sorted(flatten(list_vals))
flatten_table({'hi':[1,3], 'bye':[2,4]})
#b) returns
[1, 2, 3, 4]

#24. Define a function called file_words that takes a lename and 
returns a
#list containing all the whitespace-separated words in the file.

#a)
def file_words(text_file):
        words=[]
        for line in open(text_file):
                for word in line.split():    
                        words.append(word)   
        print words
        
#b)
file_words('foo.txt')
['This', 'is', 'test', '#2.', 'THE', 'END']

#25. Define a function called ingwords that takes a text (either an 
NLTK Text
#object or a list of strings) and returns an alphabetically sorted 
list of the
#words in it that end with \ing." 

#A)
def ingwords(list_strings):
        ing_words=[]    
        for word in list_strings:
                if "ing" in word:
                        ing_words.append(word)
        return sorted(set(ing_words))
ingwords(['hi', 'working', 'fishing', 'working', 'bye'])
#returns ['fishing', 'working']

#b) 
ingwords(text1)[:5]
['According', 'Accordingly', 'Anything', 'Assuming', 'Availing']

#26. Write a function called byfirst that takes a text (or a list of 
strings)
#as input, and produces a table in which each word is indexed by its 
rst
#letter
#a) 
table = {}
def byfirst(list_of_strs):
        for word in list_of_strs:
                table[word[0]] = word
        return table
a['i'] 
#returns 
'is'

#b)  
print_table(byfirst(text1[100:120]))
a a
b be
c called
f fish
i in
l leaving
n name
o out
t tongue
w whale


#27. Define a word to be a \likely adjective" if it also appears with 
the suffix -ly.
#For example, if \quick" and \quickly" both occur in a text, then 
\quick"
#is a likely adjective. Write a function called likely that takes a 
text and
#returns a list of likely adjectives (in alphabetic order).

#a)
def likely(text_obj):
        vocabulary = set(text_obj)                
        adjectives = []
        for word in vocabulary:
                if word[-2:] == "ly":
                        adjectives.append(word.strip("ly"))
        return sorted(adjectives)
#NOTE this returns LIKELY adjectives meaning some words will be 
nonsense because this is not eliminating terms that are not 
adjectives, rather are likely adjs.

#b)
likely(text1)[:10]
['According', 'App', 'Assured', 'Ba', 'Carefu', 'Certain', 'Common', 
'Consequent', 'Convulsive', 'Deliberate']
#returns all caps because I called sorted on the method and uppercase 
letters have prescedence in terms of order over lowercase letters.

