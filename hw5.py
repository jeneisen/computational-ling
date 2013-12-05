def firsts(word_list):
    new = []
    for word in word_list:
        new += word[0]
    return ''.join(new)

def nthlets(i, list_of_words):
    nth = []
    for element in list_of_words:
        if len(element) > i:
            nth += element[i]
        else:
            nth += " "
    return ''.join(nth)

def make_cat(string):
    quotes = " "
    if quotes in string:
        return string.strip("")
    else:
        return Nonterminal(string)

def make_rule(string_rule):
    elements = string_rule.split()
    lhs = make_cat(elements[0])
    rhs = []
    for elt in elements[2:]:
        n = make_cat(elt)
        rhs.append(n)
    if elements[1] != '->':
        raise Exception, 'Second token is not an arrow'
    rule = Production(lhs, rhs)
    return rule
        

def rule_replace(rule, string1, string2):
    n1 = Nonterminal(string1)
    n2 = Nonterminal(string2)
    results = []
    if rule.lhs() == n1:
        lhs = n2
    else:
        lhs = rule.lhs()
    for elt in rule.rhs():
        if elt == n1:
            results.append(n2)
        else:
            results.append(elt)
    p = Production(lhs, results)
    return p

def grammar_replace(grammar, str1, str2):
    n1 = Nonterminal(str1)
    n2 = Nonterminal(str2)
    out = []
    for rule in grammar.productions():
        out.append(rule_replace(rule, str1, str2))
    g = ContextFreeGrammar(Nonterminal('S'), out)
    return g


def first_pos(tree):
    speech_list = []
    for child in tree:
        if isinstance(child, Tree):
            speech_list.extend(child.pos())
        else:
            speech_list.append((child, tree.node))
    for elt in speech_list:
        return elt[1]



from nltk import ContextFreeGrammar
rule =make_rule('S -> NP VP')
rule1 =make_rule('VP -> V NP')
rule2 = make_rule('NP -> "Fido"')
rule3 = make_rule('V -> "chased"')
rules = []
rules.append(rule)
rules.append(rule1)
rules.append(rule2)
rules.append(rule3)
g = ContextFreeGrammar(Nonterminal('S'), rules)
#print g
#Grammar with 4 productions (start state = S)
#    S -> NP VP
#    VP -> V NP
#    NP -> "Fido"
#    V -> "chased"
