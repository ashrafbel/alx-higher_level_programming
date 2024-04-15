#!/usr/bin/python3
"Module defined Mylist class"


class MyList(list):
    "Medoth to print sorted"
    def print_sorted(self):
        sorte_d = sorted(self)
        print(sorte_d)
