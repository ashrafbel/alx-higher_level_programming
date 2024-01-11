#!/usr/bin/python3
def search_replace(my_list, search, replace):
    L = list(map(lambda Y: replace if Y == search else Y, my_list))
    return (L)
