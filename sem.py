from __future__ import division

from nltk import parse_fcfg, FeatureChartParser, parse_valuation, Model, Assignment, LogicParser


class Sent (object):

    def __init__ (self, dev, i, words):
        self.dev = dev
        self.i = i
        self.words = words
        self.tree = None
        self.sem = None
        self.value = None
        self.errors = []
        self.chart = None

    def parse (self):
        self.tree = None
        self.sem = None
        self.value = None
        self.errors = []
        self.chart = None
        try:
            self.tree = self.dev.parser.parse(self.words)
        except Exception, e:
            self.errors.append('(parser) ' + str(e))

        if self.tree is None:
            self.compute_chart()
        else:
            self.interpret()

    def interpret (self):
        self.sem = None
        self.value = None
        if self.tree and 'v' in self.tree.node:
            self.sem = self.tree.node['v']
            if self.sem:
                try:
                    self.value = self.dev.evaluate(self.sem)
                except Exception, e:
                    self.errors.append('(evaluation) ' + str(e))

    def compute_chart (self):
        c = self.dev.parser.chart_parse(self.words)
        d = {}
        self.chart = []
        for e in c:
            if e.is_complete() and e.rhs() and e.length() > 0:
                if e.span() in d: d[e.span()].append(e)
                else: d[e.span()] = [e]
        for span in sorted(d):
            self.chart.append(' '.join(self.words[span[0]:span[1]]))
            for e in d[span]:
                rhs = [repr(cat) for cat in e.rhs()]
                self.chart.append('    %s -> %s' % (repr(e.lhs()), ' '.join(rhs)))

    def __repr__ (self):
        lines = []
        sent = ' '.join(self.words)
        if self.i is None:
            lines.append(sent)
        else:
            lines.append('[%d] %s' % (self.i, sent))
        lines.append('parsed: %s' % bool(self.tree))
        if self.tree is None:
            lines.append('sem: (no parse)')
            lines.append('val: (no parse)')
        elif self.sem is None:
            lines.append('sem: (no translation)')
            lines.append('val: (no translation)')
        else:
            lines.append('sem: ' + str(self.sem))
            lines.append('val: ' + str(self.value))
        return '\n'.join(lines)

    def __str__ (self):
        lines = [repr(self)]
        for error in self.errors:
            lines.append('error: ' + error)
        if self.tree:
            lines.append('tree:')
            lines.append(str(self.tree))
        elif self.chart:
            lines.append('chart:')
            lines.extend(self.chart)
        return '\n'.join(lines)


#--  Dev  ----------------------------------------------------------------------

class Dev (object):

    def __init__ (self, prefix='hw-07'):
        self.prefix = prefix
        self.sents = None
        self.grammar = None
        self.parser = None
        self.model = None
        self.assignment = None
        self.i = 0
        self.lp = LogicParser()
        self.tmpsent = None

        self.reload()


    def __getitem__ (self, i):
        return self.sents.__getitem__(i)

    def reload (self):
        self.load_sents()
        self.load_grammar()
        self.load_model()
        self.parse_all()

    def load_sents (self):
        self.sents = [Sent(self, i, sent) for i, sent in self.iter_sents()]

    def iter_sents (self):
        fn = self.prefix + '-sents.txt'
        i = 0
        for line in open(fn):
            fields = line.split()
            if fields[0] != str(i):
                raise Exception, "%s: Line %d: Incorrectly numbered %s" % (fn, i, fields[0])
            yield (i, fields[1:])
            i += 1
        
    def load_grammar (self):
        fn = self.prefix + '-grammar.txt'
        self.grammar = parse_fcfg(open(fn))
        self.parser = FeatureChartParser(self.grammar)

    def parse_all (self):
        for sent in self.sents:
            sent.parse()
        if self.tmpsent:
            self.tmpsent.parse()

    def load_model (self):
        self.model = None
        self.assignment = None
        try:
            fn = self.prefix + '-model.txt'
            val = parse_valuation(open(fn).read())
            self.model = Model(val.domain, val)
            self.assignment = Assignment(self.model.domain)
        except Exception, e:
            print '** Failure loading model: ' + str(e)

    def evaluate (self, e):
        if not self.model:
            raise Exception, 'No model'
        return self.model.satisfy(e, self.assignment)

    def value (self, s):
        e = self.lp.parse(s)
        return self.evaluate(e)

    def print_sents (self):
        print 'SENTENCES:'
        for sent in self.sents:
            print
            print repr(sent)

    def __str__ (self):
        lines = []
        for sent in self.sents:
            lines.append('')
            lines.append(repr(sent))
        return '\n'.join(lines)

    def print_sent (self):
        if self.tmpsent: sent = self.tmpsent
        else: sent = self.sents[self.i]
        print
        print sent

    def step_forward (self):
        self.tmpsent = None
        self.i += 1
        if self.i >= len(self.sents): self.i = 0

    def step_back (self):
        self.tmpsent = None
        self.i -= 1
        if self.i < 0: self.i = len(self.sents) - 1

    def goto (self, i):
        self.tmpsent = None
        if i < 0: i += len(self.sents)
        if i < 0 or i >= len(self.sents):
            raise KeyError, 'Sentence number out of bounds'
        self.i = i

    def looks_like_sent (self, s):
        for word in s.split():
            if not word.isalpha(): return False
            elif not (word.islower() or word.istitle()): return False
        return True

    def parse (self, s):
        sent = Sent(self, None, s.split())
        sent.parse()
        return sent

    def save_translations (self):
        fn = self.prefix + '-trans.txt'
        out = open(fn, 'w')
        for sent in self.sents:
            out.write('%d %s\n' % (sent.i, sent.sem))
        out.close()

    def usage (self):
        print 'COMMANDS:'
        print 'r           Reload the grammar and sentences, and reparse'
        print 'n           Next: go forward one sentence'
        print 'p           Previous: go back one sentence'
        print '(a number)  Go to the sentence with that number'
        print '(an expr)   Evaluate the expression in the model'
        print '(sentence)  Parse and evaluate a temporary sentence'
        print 'c           Print current sentence (discard temp sent, if any)'
        print 'g           Print the grammar'
        print 'm           Print the model'
        print 's           Print the sentences'
        print 't           Save the translations to %s-trans.txt' % self.prefix
        print 'h           Print this message'
        print '^D          Quit'

    def run (self):
        self.usage()
        print
        self.print_sents()
        print
        self.print_sent()
        while True:
            try:
                print
                com = raw_input('> ')
                if com == 'h' or com == '' or com == '?':
                    self.usage()
                elif com == 'r':
                    self.reload()
                    self.print_sent()
                elif com == 'c':
                    self.tmpsent = None
                    self.print_sent()
                elif com == 'p':
                    self.step_back()
                    self.print_sent()
                elif com == 'n':
                    self.step_forward()
                    self.print_sent()
                elif com == 'g':
                    print self.grammar
                elif com == 's':
                    self.print_sents()
                elif com == 't':
                    self.save_translations()
                    print 'Wrote translations to %s-trans.txt' % self.prefix
                elif com == 'm':
                    self.print_model()
                elif com.isdigit():
                    self.goto(int(com))
                    self.print_sent()
                elif len(com) == 1:
                    raise Exception, 'Unrecognized command'
                elif self.looks_like_sent(com):
                    self.tmpsent = self.parse(com)
                    self.print_sent()
                else:
                    print self.value(com)
            except EOFError:
                print
                break
            except Exception, e:
                print '**', str(e)


dev = Dev()
