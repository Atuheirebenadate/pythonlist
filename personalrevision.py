# .Write a Python program to calculate the length of a string.
def word(a):
    b=0
    for c in a:
      b+=1
    print(b) 
# word("python is a good language")    

# Write a Python program to count the number of characters (character frequency) in a string
# def char_frequency(w):
#     dict = {}
#     for n in w:
#         keys = dict.keys()
#         if n in keys:
#             dict[n] += 1
#         else:
#             dict[n] = 1
# print((dict))("this word is new to me")
# 3. Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string
#4. Given a string, write a python function to check if it is palindrome or not.
#  A string is said to be palindrome if the reverse of the string is the same as string. For example, “radar” is a palindrome, but “radix” is not a palindrome
def isPalindrom(p):
    p="benadate"
    w=isPalindrom(p)
    if w:
        print("yes")
    else:
            print("not")
    print( p==p[::-1] )    
   




        

