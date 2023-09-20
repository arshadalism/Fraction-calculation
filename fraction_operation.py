import math


class Fraction:

    def __init__(self, n, d):
        self.num = n
        self.den = d

    def __str__(self):
        if self.num == 0:
            return "0"
        return f"{self.num}/{self.den}"

    def __add__(self, other):
        temp_num = self.num * other.den + other.num * self.den
        temp_den = self.den * other.den

        return Fraction(temp_num, temp_den).reduce()

    def __sub__(self, other):
        temp_num = self.num * other.den - other.num * self.den
        temp_den = self.den * other.den

        return Fraction(temp_num, temp_den).reduce()

    def __mul__(self, other):
        temp_num = self.num * other.num
        temp_den = self.den * other.den

        return Fraction(temp_num, temp_den).reduce()

    def __truediv__(self, other):
        temp_num = self.num * other.den
        temp_den = self.den * other.num

        return Fraction(temp_num, temp_den).reduce()

    def __eq__(self, other):
        return self.den * other.num == self.num * other.den

    def __lt__(self, other):
        return Fraction(self.num * other.den < other.num * self.den).reduce()

    def __le__(self, other):
        return Fraction(self.num * other.den <= other.num * self.den).reduce()

    def __gt__(self, other):
        return Fraction(self.num * other.den > other.num * self.den).reduce()

    def __ge__(self, other):
        return Fraction(self.num * other.den >= other.num * self.den).reduce()

    def reduce(self):
        common_factor = math.gcd(self.num, self.den)
        return Fraction(self.num // common_factor, self.den // common_factor)


x = Fraction(3, 4)
y = Fraction(5, 6)
print(f"x = {x}")
print(f"y = {y}")
print(f"x+y = {x + y}")
print(f"x-y = {x - y}")
print(f"x*y = {x * y}")
print(f"x/y = {x / y}")
print(x == y)
