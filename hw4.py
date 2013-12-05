#1. Define the function make_parser (Handout 8, #8). 
#a. Show the definition. Save it in the file cfg.py.
from nltk import parse_cfg
from nltk import ChartParser

def make_parser(file):
        g1 = parse_cfg(open(file))
        parser = ChartParser(g1)  
        sent = "Mary walked the dog".split()
        s = parser.parse(sent)
        print s


#b. Show any import statements you need to include in cfg.py.
from nltk import parse_cfg
from nltk import ChartParser

#2. Use make_parser to create a parser for g1, and use it to parse the 
sentence Mary walked the dog. 
#Get python to show you the tree in a readable form. (Show what you type 
to python, and the result that you get.)
make_parser('g1')
(S (NP (Name Mary)) (VP (V walked) (NP (Det the) (N dog))))


#3. Define a function called parse_sents. 
#It should take a parser and a list of strings as input. 
#For each string, it should print an empty line, then print the string. 
#Then it should parse the string and print the parse tree. For example:

def parse_sents(parser, list_strs):
    for sent in list_srts:
        print  parse(sent)
    

def load_sents(file):
    out = []
    for sent in open(file):
        out.append(sent)
    print out

def testg(file, text_file):
    p = make_parser(file)
    sents = load_sents(text_file)
    parse_sents(p, sents)
