#!/usr/bin/python3
"Module def square class"
from models.rectangle import Rectangle


class Square(Rectangle):
    "class square"
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        "Provides string info about this rectangle"
        square_str = f"[Square] ({self.id}) {self.x}/{self.y} - "
        square_str += f"{self.width}"
        return square_str

    @property
    def size(self):
        "size of rect"
        sz = self.width
        return sz

    @size.setter
    def size(self, val):
        "square setter"
        self.width = val
        self.height = val
    
    def update(self, *args, **kwargs):
        "update instance by using args/kwargs"
        if args:
            A = ["id", "size", "x", "y"]
            for n, ag in enumerate(args):
                setattr(self, A[n], ag)
        elif kwargs:
            for K, val in kwargs.items():
                setattr(self, K, val)
