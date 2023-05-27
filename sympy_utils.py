from sympy import (
    AtomicExpr, sympify, Integer, Rational, NumberSymbol, dotprint,
    Basic, Equality, Expr, Derivative, Integral, simplify, collect,
    collect_const, expand, factor, symbols, GreaterThan, sin, lambdify
)
from sympy.core.add import _unevaluated_Add, Add
from sympy.core.decorators import _sympifyit
from sympy.core.evalf import EvalfMixin
from sympy.core.relational import Relational
from sympy.printing import latex
from sympy.printing.pretty.stringpict import prettyForm
import mpmath.libmp as mlib
import math
from graphviz import Source
import unittest as ut
import numpy as np


################################################################################
############################## CONSTANT NUMBERS ################################
################################################################################

class Constant(NumberSymbol):
    """ Represent a generic integer or float constant: it will be treaded as a 
    symbol during symbolic computations, whereas it will be converted to a 
    number during numerical evaluation.

    Examples
    ========

    t = Constant(2.5, r"\tau")
    display(t, t.evalf(), t + 2)
    """
    is_real = True

    def __new__(cls, value, name, latex="", pretty=""):
        """
        Parameters
        ----------
            value : float
                The numerical value of the constant
            name : string
                Used to render the symbol when calling print()
            latex (optional) : string
                Latex code representing representing this constant. If not
                provided, `name` will be used instead.
            pretty (optional) : string
                Used to render the symbol when calling pprint(). Unicode strings
                are admissible. If not provided, `name` will be used instead.
        """
        if isinstance(value, Integer):
            value = value.p
        if not isinstance(value, (int, float)):
            raise TypeError("'value' must be a Python's int or float. \n" +
                "Instead, got {}".format(type(value)))
        if not all([isinstance(a, str) for a in [name, latex, pretty]]):
            raise TypeError("Parameters name, latex, pretty must be of type string")
        
        obj = AtomicExpr.__new__(cls)
        obj._value = value
        obj._name = name
        obj._latex_str = latex
        obj._pretty_str = pretty
        return obj

    def _as_mpf_val(self, prec):
        return mlib.from_float(self._value, prec)

    def approximation_interval(self, number_cls):
        if issubclass(number_cls, Integer):
            return (Integer(math.floor(self._value)), Integer(math.ceil(self._value)))
        elif issubclass(number_cls, Rational):
            pass
    
    def _latex(self, printer):
        if self._latex_str:
            return self._latex_str
        return self._name
    
    def _sympyrepr(self, printer, *args):
        return (self.func.__name__ + 
            "(value={}, name='{}', latex='{}', pretty='{}')".format(
                self._value, self._name, self._latex_str, self._pretty_str
            ))

    def _sympystr(self, printer, *args):
        return self._name

    def _pretty(self, printer, *args):
        if printer._use_unicode and self._pretty_str:
            return prettyForm(self._pretty_str)
        return prettyForm(self._name)


################################################################################
################################## UTILITIES ###################################
################################################################################

def render_tree(expr, filename, format="png"):
    """ Show the expression tree. This function saves in the current folder two
    files associated to `expr`:
        1. filename.gv: contains the DOT representation.
        2. filename.png: the DOT representation has been rendered and saved into 
            this image.

    Parameters
    ----------
        expr : the symbolic expression
        filename : string
            The name of the generated files.
        format : string
            The format of the output image. Default to "png".
    """
    if not isinstance(filename, str):
        raise TypeError("'filename' must be of type str. " + 
            "Instead, got: {}".format(type(filename)))
    s = Source(dotprint(expr), filename=filename + ".gv", format=format)
    s.view()
