#!/usr/bin/python3
"""class Myint"""


class MyInt(int):
    """MyInt class that inherits"""
    def __eq__(self, other):
        """Reverse the == operator's behavior"""
        return super().__ne__(other)

    def __ne__(self, other):
        """"Adjust the != operator to invert its meaning"""
        return super().__eq__(other)
