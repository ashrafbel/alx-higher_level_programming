def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    else:
        MAX = max(a_dictionary, key=a_dictionary.get)
        return MAX
