from nltk import parse_cfg
from nltk import ChartParser

def make_parser(file):
    global parser
        g1 = parse_cfg(open(file))
        parser = ChartParser(g1)  
        return parser

def parse_sents(parser, list_strs):
        for phrase in list_strs:
        phr = phrase.split()
        print "\n", phrase, parser.parse(phr)

def load_sents(file):
        out = []
        for sent in open(file):
        out.append(sent)    
    return out

def testg(file, text_file):
    p = make_parser(file)
    sentences = load_sents(text_file)
    parse_sents(p,sentences)



def collect_leaves(tree, list):
        if isinstance(tree, str):
                return [tree]
        else:
        for child in tree:
            list.append(collect_leaves(child, list))

def leaves(tree):
    x = []
    print collect_leaves(tree, x)

from nltk import Production, Nonterminal
def tree_rules(tree):
    rules = tree.productions()
    return rules

from nltk import Production, Nonterminal
def tree_cat(tree):
    if type(tree) == str:
        print tree
    else:
        lhs = Nonterminal(tree.node)
        return lhs

def tree_rule(tree):
    rules = tree.productions()
    for r in rules:
        if r.lhs() == Nonterminal(tree.node): 
            print r
        

def collect_tree_rules(tree, list):
    rules = tree.productions()
    for r in rules:
        list.append(r)

def tree_rules(tree):
    return tree.productions()
