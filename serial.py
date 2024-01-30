"""Python serial number generator."""

class SerialGenerator:
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


    def __init__(self, start):
        "Constructor for SerialGenerator, accepts the starting serial number"
        self.serial = start - 1
        self.start = start

    def generate(self):
        "Generate and return the next sequence serial number"
        self.serial = self.serial+1
        return self.serial
    
    def reset(self):
        "Reset to the original starting number"
        self.serial = self.start - 1


