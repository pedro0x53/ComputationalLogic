from FOLFormulas import *
from FOLTerms import *

class FOLFormatter:
    def __init__(self):
        pass

    def replace(self, term, old, new):
        if term == old:
            return new

        if isinstance(term, Func):
            return Func(term.name, [self.replace(arg, old, new) for arg in term.args])

        if isinstance(term, Atom):
            return Atom(term.name, [self.replace(arg, old, new) for arg in term.args])

        if isinstance(term, Not):
            return Not(self.replace(term.inner, old, new))

        if isinstance(term, And):
            return And(self.replace(term.left, old, new), self.replace(term.right, old, new))

        if isinstance(term, Or):
            return Or(self.replace(term.left, old, new), self.replace(term.right, old, new))

        if isinstance(term, Implies):
            return Implies(self.replace(term.left, old, new), self.replace(term.right, old, new))

        if isinstance(term, ThereExists) and term.variable != str(new):
            return self.replace(term.inner, old, new)

        if isinstance(term, ForAll) and term.variable != str(new):
            return self.replace(term.inner, old, new)

        return term