"""
#----------------------ODD OR EVEN---------------------------------------------
num=int(input("Enter the number:"))
if(num%2==0):
    print("Number is Even")
else:
    print("Number is Odd")

    

#--------------------------lARGEST OF 3 NUMBERS---------------------------------
a=int(input("Enter first Number:"))
b=int(input("Enter second Number:"))
c=int(input("Enter third Number:"))

if(a>b and a>c):
    print(a," is largest number")
elif(b>a and b>c):
     print(b," is largest number")
else:
     print(c," is largest number")



#----------------------------LEAP YEAR-------------------------------------------
year = int(input("Enter the year"))

if(year%4==0 and year%100!=0):
    print("Leap Year")
elif(year%400==0 and year%100==0):
    print("Leap Year")    
else:
    print("Non-Leap Year")


#------------------------ SUMMING NUMBERS----------------------------------
num=int(input("Enter the number:"))
sum=0
while(num>0):
    sum+=num
    num-=1
print("Sum is:" ,sum)





#------------------------COUNT DOWN-------------------------------------
num=int(input("Enter the number:"))
while(num>0):
    print(num);
    num-=1;
    

"""
