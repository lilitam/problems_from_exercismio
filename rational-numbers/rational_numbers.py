from __future__ import division
from math import gcd

class Rational(object):
    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom

    def __eq__(self, other):
        gdc_self = gcd(self.numer, self.denom)
        gdc_other = gcd(other.numer, other.denom)
        self_numer = self.numer / gdc_self
        self_denom = self.denom / gdc_self
        other_numer = other.numer / gdc_other
        other_denom = other.denom / gdc_other
        return self_numer == other_numer and self_denom == other_denom

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        return Rational(self.numer * other.denom + other.numer * self.denom, self.denom * other.denom)

    def __sub__(self, other):
        return Rational(self.numer * other.denom - self.denom * other.numer, self.denom * other.denom)

    def __mul__(self, other):
        return Rational(self.numer * other.numer, self.denom * other.denom)

    def __truediv__(self, other):
        return Rational(self.numer * other.denom, self.denom * other.numer)

    def __abs__(self):
        self.numer = abs(self.numer)
        self.denom = abs(self.denom)
        return Rational(self.numer, self.denom)

    def __pow__(self, power):
        return Rational(self.numer ** power, self.denom ** power)

    def __rpow__(self, base):
        pass
