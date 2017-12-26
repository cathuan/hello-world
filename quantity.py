class Quantity(object):

    buffered = {}

    def __new__(cls, q):
        #assert isinstance(q, int)  # FIXME: should we do this?
        if q in Quantity.buffered:
            return Quantity.buffered[q]
        else:
            obj = super(Quantity, cls).__new__(cls)
            obj.quantity = q
            Quantity.buffered[q] = obj
            return obj

    def __lt__(self, other):
        assert isinstance(other, Quantity)
        return self.quantity < other.quantity

    def __le__(self, other):
        assert isinstance(other, Quantity)
        return self.quantity <= other.quantity

    def __eq__(self, other):
        assert isinstance(other, Quantity)
        return self.quantity == other.quantity

    def __ne__(self, other):
        assert isinstance(other, Quantity)
        return self.quantity != other.quantity

    def __ge__(self, other):
        assert isinstance(other, Quantity)
        return self.quantity >= other.quantity

    def __gt__(self, other):
        assert isinstance(other, Quantity)
        return self.quantity > other.quantity

    def __neg__(self):
        return Quantity(-self.quantity)

    def __add__(self, other):
        assert isinstance(other, Quantity)
        return Quantity(self.quantity + other.quantity)

    def __sub__(self, other):
        assert isinstance(other, Quantity)
        return Quantity(self.quantity - other.quantity)

    def __mul__(self, other):
        assert isinstance(other, int) or isinstance(other, float)
        return Quantity(self.quantity * other)

    def __rmul__(self, other):
        assert isinstance(other, int) or isinstance(other, float)
        return Quantity(self.quantity * other)

    def __mod__(self, other):
        assert isinstance(other, Quantity)
        return Quantity(self.quantity % other.quantity)

    def __div__(self, other):
        if isinstance(other, Quantity):
            return self.quantity * 1.0 / other.quantity
        elif isinstance(other, int):
            return Quantity(self.quantity / other)
        assert False

    def __truediv__(self, other):
        assert False  # TODO: not implement with division when __future__.division is imported

    def __abs__(self):
        return Quantity(abs(self.quantity))

    def __repr__(self):
        return str(self.quantity)

    def to_float(self):
        return self.quantity

    def mul_price_quantity(self, price):
        return price * self.quantity


if __name__ == "__main__":

    q1 = Quantity(3)
    q2 = Quantity(3)
    print q1, q2
    print type(q1), type(q2)
    print id(q1), id(q2), q1 is q2
