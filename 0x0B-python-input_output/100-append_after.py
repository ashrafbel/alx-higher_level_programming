#!/usr/bin/python3
def append_after(filename="", search_string="", new_string=""):
    "Inserts text after each line with a specific string in a file."
    with open(filename, 'r') as Fl:
        li_nes_txt = Fl.readlines()

    with open(filename, 'w') as Fl:
        for Ln in li_nes_txt:
            Fl.write(Ln)
            if search_string in Ln:
                Fl.write(new_string)
