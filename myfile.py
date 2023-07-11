import turtle
import random
a=set("абвгдежзийклмнопрстуфхцчшщыьэюяabcdefghijklmnopqrstuvwxyz")
l=["hi","man"]
w=random.choice(l)
s=0
o=set()
x=len(w)
print("enter word,lenght=",x)
k="_"*x
print(k)
m=list(w)
while s<11:
    if set(w)==o:
        print("you win")
        print(w)
        break
    i=str(input("enter one letter of the word or full word:"))
    if len(i)==1 or len(i)==x:
        if set(i)==set(w):
            print("you win")
            print(w)
            break
        else:
            if i in w:
                print("true")
                o.add(i)
                new=""
                
                for h in range(len(w)):
                    if i==w[h]:
                        new+=i
                    else:
                        new+=k[h]
                k=new
                print(k)
                        
                if i in a:
                    a=a-set(i)
                else:
                    print("you have used this letter")
            else:
                print("no")
                s=s+1
                if i in a:
                    a=a-set(i)
                if i in o:
                    print("you have used this letter")
        
    else:
        print("you can't")
    if s >=11:
        print("you have killed")

            
