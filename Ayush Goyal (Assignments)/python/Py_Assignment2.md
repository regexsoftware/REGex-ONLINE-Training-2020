# Assignment 2 [Python] [Ayush Goyal]

## 1. What should be the output? ( 3 + 4 ** 6 - 9 * 10 / 2 )


```python
3 + 4 ** 6 - 9 * 10 / 2
```




    4054.0



## 2. Let say I have, some string "hello this side regex"
- Find out the count of the total vowels
- vowels - ['a','e','i','o','u']


```python
string = "hello this side regex"
vowels = ['a', 'e', 'i', 'o', 'u']

count = 0

for word in string:
    alphabets = word.split()
    for x in alphabets:
        if x in vowels:
            count += 1
            
print(count)
```

    7


## 3. Find out the area of triangle


```python
print("Base :")
b = int(input())

print("Height :")
h = int(input())

print("Area = ", end = " ")
print((1/2)*b*h)
```

    Base :
    4
    Height :
    5
    Area =  10.0


## 4. Print Calendar of a year


```python
import calendar

print("Year", end = " ")
y = int(input())

print("Calendar \n\n\n")
print(calendar.calendar(y))
```

    Year 2020
    Calendar 
    
    
    
                                      2020
    
          January                   February                   March
    Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
           1  2  3  4  5                      1  2                         1
     6  7  8  9 10 11 12       3  4  5  6  7  8  9       2  3  4  5  6  7  8
    13 14 15 16 17 18 19      10 11 12 13 14 15 16       9 10 11 12 13 14 15
    20 21 22 23 24 25 26      17 18 19 20 21 22 23      16 17 18 19 20 21 22
    27 28 29 30 31            24 25 26 27 28 29         23 24 25 26 27 28 29
                                                        30 31
    
           April                      May                       June
    Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
           1  2  3  4  5                   1  2  3       1  2  3  4  5  6  7
     6  7  8  9 10 11 12       4  5  6  7  8  9 10       8  9 10 11 12 13 14
    13 14 15 16 17 18 19      11 12 13 14 15 16 17      15 16 17 18 19 20 21
    20 21 22 23 24 25 26      18 19 20 21 22 23 24      22 23 24 25 26 27 28
    27 28 29 30               25 26 27 28 29 30 31      29 30
    
            July                     August                  September
    Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
           1  2  3  4  5                      1  2          1  2  3  4  5  6
     6  7  8  9 10 11 12       3  4  5  6  7  8  9       7  8  9 10 11 12 13
    13 14 15 16 17 18 19      10 11 12 13 14 15 16      14 15 16 17 18 19 20
    20 21 22 23 24 25 26      17 18 19 20 21 22 23      21 22 23 24 25 26 27
    27 28 29 30 31            24 25 26 27 28 29 30      28 29 30
                              31
    
          October                   November                  December
    Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
              1  2  3  4                         1          1  2  3  4  5  6
     5  6  7  8  9 10 11       2  3  4  5  6  7  8       7  8  9 10 11 12 13
    12 13 14 15 16 17 18       9 10 11 12 13 14 15      14 15 16 17 18 19 20
    19 20 21 22 23 24 25      16 17 18 19 20 21 22      21 22 23 24 25 26 27
    26 27 28 29 30 31         23 24 25 26 27 28 29      28 29 30 31
                              30
    


____
