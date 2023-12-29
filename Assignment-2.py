"""
#Q.Write a program to  create a list of fruits and copy only 'e' letter fruits to the new list
fruits=["mango","pappaya","pineapple","cherry","orange","apple","kiwi"]
newfruits=[]
for i in fruits:
    for x in i:
        if(x=="e"):
            newfruits.append(i)
            break        
print(newfruits)

#---------------------------------------------------------------------------------------------------

#Q. ⁠write Pgm to find prime number or not
flag=0
num=int(input("Enter number: "))
for i in range(1,(n//2)):
    if(num%i==0):
        flag=1
    else:
        flag=0
if(flag==1):
    print("number is not prime")
else:
    print("number is prime")
"""
