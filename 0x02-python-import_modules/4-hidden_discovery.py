#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4

    NAMES = dir(hidden_4)
    for X in NAMES:
        if X[:2] != "__":
            print(X)
