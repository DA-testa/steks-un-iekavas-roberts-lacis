# python3

from collections import namedtuple
#from tkinter import filedialog     //Importējam TKinter lai izmantotu failu atvēršanas dialogu. Komentēts, jo github neatbalsta TKinter


Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(txt):
    opening_brackets_stack = []
    for i, next in enumerate(txt):
        if next in "([{":
            opening_brackets_stack.append(next)
            pass

        if next in ")]}":
            if len(opening_brackets_stack) != 0:
                if are_matching(opening_brackets_stack[-1], next):
                    opening_brackets_stack = opening_brackets_stack[:-1]
                else:
                    return i+1
            else:
                return i+1
            pass
    if len(opening_brackets_stack) != 0:
        return txt.find(opening_brackets_stack[0])+1
    return "Success"


def main():
    var = input()
    a=input()
    text=""
    #if var == "I":
     #   text = input()    
#    else:                                                                  //GITHUB neatbalsta TKinter
#        file_path_string = filedialog.askopenfilename()
#        file = open(file_path_string)
#        text = file.read()
    mismatch = find_mismatch(text)
    print(mismatch)


if __name__ == "__main__":
    main()