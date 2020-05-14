#Python Class 3:
#1)Find the Armstrong Number between the two numbers which are input by user
#Armstrong number : 153 -> 1*1*1 + 5*5*5 + 3*3*3
#ans
num = int(input("Enter a number: "))
sum = 0
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10
if num == sum:
    print(num,"is an Armstrong number")
else:
    print(num,"is not an Armstrong number")

#2Let’s say you have a string “hello this world @2020!!! ”
#Remove the punctuation like [“@!#$%&*()”] from the string
# Final output should be without the punctuation
# “hello this world 2020”

#ans
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
my_str = 'hello this world @2020!!!'
no_punct = ""
for char in my_str:
    if char not in punctuations:
        no_punct = no_punct + char
print(no_punct)

# You have a list with words - [“Apple”, “banana”, “cat”, “REGEX”,”apple”]
# Sort words in Alphabetical order
#If you get output, like [Apple, apple, banana]
# How has it happened?
o =['Apple', 'banana', 'cat', 'REGEX','apple']
o.sort()
print(o)
