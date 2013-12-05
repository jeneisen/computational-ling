from __future__ import division

import nltk, random, os
from nltk.featstruct import unify
from nltk.tree import Tree
from nltk.parse.featurechart import FeatureChartParser
from nltk.grammar import parse_fcfg


DataDir = os.path.join(os.getenv('CL'), 'data')

def iter_frontier (tree):
    if isinstance(tree, str):
        yield tree
    else:
        for child in tree:
            for leaf in iter_frontier(child):
                yield leaf

def frontier (tree):
    return list(iter_frontier(tree))

def frontier_string (tree):
    return ' '.join(frontier(tree))


def is_sentence_over (s, vocab):
    for w in s:
        if w not in vocab:
            return False
    return True


def generate_n (g, n=10, maxlen=20, vocab=None):
    sents = []
    tries = 0
    while len(sents) < n:
        if tries > n * 10:
            raise Exception, "Too many tries"
        tries += 1
        s = generate(g)
        if maxlen and len(s) > maxlen:
            continue
        if vocab and not is_sentence_over(s, vocab):
            continue
        sents.append(s)
    return sents
        

def generate (g):
    t = generate_tree(g)
    return frontier(t)


class Failure (Exception):
    pass

def generate_tree (g, ntries=100):
    if isinstance(g, nltk.parse.api.ParserI):
        g = g.grammar()
    for i in range(ntries):
        try:
            return generate_from(g.start(), g)
        except Failure:
            pass
    raise Exception, "Too many failures"


def iter_expansions (x, g):
    for r in g.productions(lhs=x):
        bindings = {}
        x1 = unify(x, r.lhs(), bindings, rename_vars=False)
        if x1:
            yield (r, x1, bindings)

def expansions (x, g):
    return list(iter_expansions(x, g))


def generate_from (x, g):
    options = expansions(x, g)
    if not options:
        raise Failure
    (r, x, bindings) = random.choice(options)
    children = []
    for y in r.rhs():
        if isinstance(y, str):
            children.append(y)
        else:
            y = y.substitute_bindings(bindings)
            child = generate_from(y, g)
            children.append(child)
            # just to update the bindings
            if not unify(y, child.node, bindings, rename_vars=False):
                raise Exception, "This can't happen"
    x = x.substitute_bindings(bindings).rename_variables()
    return Tree(x, children)


def load_grammar (fn):
    g = parse_fcfg(open(fn))
    g.parser = FeatureChartParser(g)
    g.parse = g.parser.parse
    return g


def grail_vocab ():
    from nltk.book import text6
    vocab = set([w.lower() for w in text6 if w.isalpha()])
    vocab.remove('an')
    return vocab


def grammar_vocab (g):
    v = set()
    for r in g.productions():
        for y in r.rhs():
            if isinstance(y, str):
                v.add(y)
    return v


def check_vocab (g, sents):
    gvocab = grammar_vocab(g)
    svocab = sents_vocab(sents)
    diff = svocab - gvocab
    if diff:
        print 'NOT COVERED BY GRAMMAR:'
        for w in sorted(diff):
            print w
        print
    diff = gvocab - svocab
    if diff:
        print 'NOT ATTESTED IN SENTS:'
        for w in sorted(diff):
            print w


def grammar_parts (g):
    v = set()
    for r in g.productions():
        z = r.rhs()
        if len(z) == 1 and isinstance(z[0], str):
            v.add(r.lhs())
    return v


def grammar_predictions (g, sents):
    return list(iter_grammar_predictions(g, sents))

def iter_grammar_predictions (g, sents):
    p = FeatureChartParser(g)
    for sent in sents:
        try:
            if p.parse(sent):
                yield 'OK'
            else:
                yield '*'
        except:
            yield '*'

def starter_grammar ():
    if DataDir is None:
        raise Exception, 'Not defined: CL'
    fn = os.path.join(DataDir, 'starter_grammar.txt')
    return nltk.parse_fcfg(open(fn))

def permitted_vocab ():
    if DataDir is None:
        raise Exception, 'Not defined: CL'
    fn = os.path.join(DataDir, 'vocab.txt')
    return set([line.rstrip('\r\n') for line in open(fn)])

def sents_vocab (sents):
    vocab = set()
    for sent in sents:
        for word in sent:
            vocab.add(word)
    return vocab

def print_sents (sents, labels=None):
    i = 0
    for sent in sents:
        sent = ' '.join(sent)
        if labels:
            print i, labels[i], sent
        else:
            print i, sent
        i += 1


def save_sents (sents, fn):
    file = open(fn, 'w')
    i = 0
    for sent in sents:
        file.write('%d %s\n' % (i, ' '.join(sent)))
        i += 1
    file.close()


def load_sents (fn):
    return list(iter_sents(fn))

def iter_sents (fn):
    i = 0
    for line in open(fn):
        fields = line.split()
        if not fields[0].isdigit():
            raise Exception, "Line must start with a number"
        if int(fields[0]) != i:
            raise Exception, "Lines must be sequentially numbered from zero"
        i += 1
        yield fields[1:]

def starter_sents ():
    return load_sents(os.path.join(DataDir, 'starter_sents.txt'))


def load_labels (fn):
    return list(iter_labels(fn))

def iter_labels (fn):
    i = 0
    for line in open(fn):
        fields = line.split()
        if not fields[0].isdigit():
            raise Exception, "Line must start with a number"
        if int(fields[0]) != i:
            raise Exception, "Lines must be sequentially numbered from zero"
        i += 1
        if len(fields) != 2:
            raise Exception, "Label must be a single word"
        yield fields[1]


def starter_labels ():
    return load_labels(os.path.join(DataDir, 'starter_labels.txt'))


def compare_labels (labels, pred):
    tp = 0
    fp = 0
    tn = 0
    fn = 0
    for l, p in zip(labels, pred):
        if l == 'OK':
            if p == 'OK': tp += 1
            else: fn += 1
        else:
            if p == 'OK': fp += 1
            else: tn += 1
    ok = tp + fn
    bad = tn + fp
    n = ok + bad
    return ((tp + tn)/n, tp/ok, tn/bad)

def print_score (labels, pred):
    acc, sens, spec = compare_labels(labels, pred)
    print 'Accuracy:   ', acc
    print 'Sensitivity:', sens
    print 'Specificity:', spec


def print_errors (sents, labels, pred):
    i = 0
    for sent, lab, plab in zip(sents, labels, pred):
        if lab != plab:
            print i, lab, ' '.join(sent)
        i += 1

        
def print_chart (g, sent):
    c = g.parser.chart_parse(sent)
    d = {}
    for e in c:
        if e.is_complete() and e.rhs() and e.length() > 0:
            if e.span() in d: d[e.span()].append(e)
            else: d[e.span()] = [e]
    for span in sorted(d):
        print ' '.join(sent[span[0]:span[1]])
        for e in d[span]:
            print '   ', repr(e.lhs()), '->',
            for cat in e.rhs(): print repr(cat),
            print
