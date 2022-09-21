class Jar:

    # __init__ should initialize a cookie jar with the given capacity,
    # which represents the maximum number of cookies that can fit in the cookie jar.
    # If capacity is not a non-negative int, though, __init__ should instead raise a ValueError.
    # adding _ infront of properties means they are private
    def __init__(self, capacity=12):
        if not isinstance(capacity, int):
            raise ValueError("capacity should be an int")
        if capacity < 0:
            raise ValueError("capacity should be a non-negative int")

        self._capacity = capacity
        self._size = 0


    # __str__ should return a str with  🍪, where  is the number of cookies in the cookie jar.
    # For instance, if there are 3 cookies in the cookie jar, then str should return "🍪🍪🍪"
    def __str__(self):
        return "🍪" * self._size


    # deposit should add n cookies to the cookie jar.
    # If adding that many would exceed the cookie jar’s capacity, though, deposit should instead raise a ValueError.
    def deposit(self, n):
        self._size = self._size + n
        if self._size > self._capacity:
            raise ValueError("too many cookies")

    def withdraw(self, n):
        self._size = self._size - n
        if self._size < 0:
            raise ValueError("not enough cookies")

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size



