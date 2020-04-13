# Question 1
'''
Find the Armstrong Number between the two numbers which are input by user
    ○ Armstrong number : 153 -> 1*1*1 + 5*5*5 + 3*3*3
'''

number1 = int(input("Enter the starting number"))
number2 = int(input("Enter the ending number"))

for i in range(number1, number2 + 1):
    sum = 0
    temp = i
    while temp > 0:
        digit = temp % 10
        sum = sum + digit ** 3
        temp = temp // 10

    if i == sum:
        print (i)
    

