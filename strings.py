# Write a python program that given a string reverse each word?
# remove duplicates in string
def remove_duplicate(s):
    a=set(s)
    a="".join(a)
    dup=""
    for i in s:
        if(i in dup):
            pass
        else:
            dup=dup+i
    print(dup)
    
s="tomorrow"
# print(s)
print(remove_duplicate(s))
    

