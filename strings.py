# Write a python program that given a string reverse each word?
# remove duplicates in string
# from tracemalloc import start


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
    
# Using two pointer function, reverse a string.

# k=""
# start=0
# end=len(a)-1
# for i in a:
#     w=a[start],a[end]
#     # a[end],a[start]=a[start],a[end]
#     w=a[end],a[start]
#     print(k.join(a))

# a="I am Akirachix"
# a.split()
# start=0
# end=len(a)-1
# while start<end:
#     a[start],a[end]=a[end],[start]
#     start+=1
#     end-=1
#     b=""
#     new=b.join(a)
#     print(new)

def word(a):
  d=a.split()
  start=0
  end=len(d)-1
  while start<end:
    d[start],d[end]=d[end],d[start]
    start+=1
    end-=1
    b=' '
  print(b.join(d))
word("i am AkiraChix")






