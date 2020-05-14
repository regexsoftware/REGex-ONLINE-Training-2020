#1 what will be the output of 3+4**6-9*10/2
#ans- exponent>multiplication=division>addition=subtraction
#=3+4**6-9*5
#=3+4096-45
#=4099-45=4054
#so by this  the answer will be 4054.
print(3+4**6-9*10/2)


#2)lets say i have a string "hello this side regex". count the total no. of vowels present in the  string.
#ans-
string=input("Enter string:")
vowels=0
for i in string:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
        vowels=vowels+1
print("Number of vowels are:",vowels)


#3)find out the area of the triangle . you have to take the value from the user about the base and the height.
#ans-
h=int(input("enter the height of the triangle="))
b=int(input("enter the base of the triangle="))
print("area of the traingle is=",(1/2)*b*h)
