"""Python serial number generator."""

class SerialGenerator:
    def __init__(self, start):
        self.start = start
        self.original = self.start
    def generate(self):
        self.start = self.start + 1
        return (self.start)
    def reset(self):
        self.start = self.original
        return (self.start)


        

    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

