class MyInt(int):
    """A class named MyInt that inherits"""

    def __eq__(self, other):
        return super().__ne__(other)

    def __ne__(self, other):
        return super().__eq__(other)
