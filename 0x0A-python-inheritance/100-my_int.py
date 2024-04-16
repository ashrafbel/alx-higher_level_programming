#!/usr/bin/python3
"""class Myint"""

class MyInt(int):
    """MyInt class that inherits"""

    def __eq__(self, other):
        """Modify the behavior of the == operator to have the opposite effect."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Modify the behavior of the != operator to have the opposite effect"""
        return super().__eq__(other)
