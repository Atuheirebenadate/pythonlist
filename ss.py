def nesting():
   list=["mango",[2,3,4,6,8],[8,8,5,6]]
   print(list[1][3])
   nesting()
def numbers():
     x=[1,2,3,4,5]
     x.remove(x[4])
     print(x)
numbers()
def number():
 numbers.remove(numbers[4])
print(numbers)
numbers()
def days():
     my_list=['monday','tuesday','wednesday','thursday','friday','monday']
     m= my_list.count('monday')
     print(m)
days()
def smallest():
    a=[3,6,8,2,4,1,5,7]
    b = min(a)
    print(b)
smallest()
def divisible__by__seven():
     b=[]
     for a in range (100,200):
       if a%7==0:
         b.append(a)
         print(b)    
divisible__by__seven()
def put_numbers():
    num1=int(input("number1"))   
    num2 = int(input("number2"))
    sum= num1+num2
    if sum>10:       
     print(f"the number is greate than 10")
    else:
       print(f"this is number is less than or equal to 10")
put_numbers()
def my_letters(a):
      a=[1,2,3,4,5]
      if 4 in a:
          print(True)
      else:
           print(False)
my_letters([1,2,3,4,5]) 
def fruit(fruits):
      fruits.remove(fruits[2])
      print (fruits)
fruit(["apple","grape","pineapple"]) 
def my_car(cars):
     cars.sort()
     print(cars)
my_car(["FORD","BMW","VOLVO"] )  
# for x in range(2.3,3.4,5.6):
#      print(x)
# Given a string,change half of a string into uppercase and return the string

def word(a):
    b = ''
    c = ''
    for i in range(int(len(a)//2 )):
        b +=  a[i]
        changed = b.upper()
        print(changed)
    for i in range(int(len(a)//2), len(a)):
          c+= a[i]

    change = changed + c
    print(change)
word("school")
word("She is playing")
word("wearehappytobeintheworld")

#  Given a list of strings check the palindrome.
def palindrome(x):

    start=0
    end=len(x)-1
    for p in x:
        if p[start]!=p[end]:
             start +=1
             end -=1

        print(f"{p}is not a palindrome")
    else:
        start +=1
        end -=1
        print(f"{p}is a palindrome")
palindrome(["mama","teacher","level","wisdom"])       

                 



      
         
         
         

          

    

 

    
             


    



    

    

        
       




