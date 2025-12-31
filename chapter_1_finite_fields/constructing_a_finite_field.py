# aim of this script is to represent an element of a finite/prime field as a class
class FieldElement:  # an element in Fp where p is a prime number
    def __init__(self, num, prime):  # num is the element, while prime is the order of the field
        if num>=prime or num<0:  # a finite field of order p looks like this: 0, 1, 2, ..., p-1.  enforcing this rule
            raise ValueError("not in range")
        self.num = num
        self.prime = prime

    # sooo, let's take a look at what does these all underscores means in functions above
    # these are NOT private methods, these are just dunder methods and does not mean private
    # __X -> private method
    # __X__ -> a special/magic/dunder method
    """these dunder methods act as a bridge between python's core and our class, allowing us to override operators 
    and built-in funcs"""
    def __repr__(self):  # only for debug
        """ also this little method is also a special method which is called when you want to print an object"""
        # print(a) -> python calls -> a.__repr__() however i override the original
        return 'FieldElement_{}({})'.format(self.prime, self.num)

    def __eq__(self, other):  # indicates when two elements of a field are equal
        if other is None:
            return False
        return self.num == other.num and self.prime == other.prime  # when they share the same field(prime) and
                                                                    # same value(num)

    # EXERCISE 1
    def __ne__(self, other):
        return not self == other  # this is brilliant like you use __eq__ in __ne__ so you dont have to check respectively


a = FieldElement(7, 13)
b = FieldElement(7, 18)
print(a==b)  # MOST CRUCIAL POINT:(OPERATOR OVERLOADING) in python normally if you use ==, python call a func called
             # __eq__but my class' func here(__eq__) overrides the original __eq__
             # even if a and b share the same value, they have different memory addresses
             # w/out FieldElement's __eq__, a==b equals false becaouse of memory,
             # but mathematically we want it to be a correct statement
print(type(a))
