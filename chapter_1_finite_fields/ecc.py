class FieldElement:
    def __init__(self, num, prime):
        if num>=prime or num<0:
            raise ValueError("not in range")
        self.num = num
        self.prime = prime

    def __repr__(self):
        return 'FieldElement_{}({})'.format(self.prime, self.num)

    def __eq__(self, other):
        if other is None:
            return False
        return self.num == other.num and self.prime == other.prime

    def __ne__(self, other):
        return not self == other

    def __add__(self, other):
        if other.prime != self.prime: raise TypeError("cannot add two numbers in different fields")
        num = (self.num + other.num) % self.prime
        return self.__class__(num, self.prime)

    def __sub__(self, other):
        if other.prime != self.prime: raise TypeError("cannot subtract two numbers in different fields")
        num = (self.num - other.num) % self.prime
        return self.__class__(num, self.prime)

    def __mul__(self, other):
        if other.prime != self.prime: raise TypeError("cannot multiply two numbers in different fields")
        num = (self.num * other.num) % self.prime
        return self.__class__(num, self.prime)

    # def __pow__(self, exponent):
    #     num = (self.num ** exponent) % self.prime
    #     return self.__class__(num, self.prime)

    def __pow__(self, exponent):
        exponent %= (self.prime-1)
        num = pow(self.num, exponent, self.prime)
        return self.__class__(num, self.prime)

    def __truediv__(self, other):
        num = (self.num * pow(other.num, self.prime-2, self.prime)) % self.prime
        return self.__class__(num, self.prime)