def cmpStringLen(s1,s2):
    if len(s1)>len(s2):
        print(s1) 
    elif len(s2)>len(s1):
        print(s2)
    else:
        print(f"{s1}\n{s2}")
    return

string1 = input("enter string 1: ")
string2 = input("enter string 2: ")

cmpStringLen(string1,string2)