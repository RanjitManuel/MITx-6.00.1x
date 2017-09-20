"""
Problem 3
15.0/15.0 points (graded)
Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh
In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc

"""

s = 'azcbobobegghakl'

index=0
lenght_longest_string=0
longest_string=""
current_idx=0

current=""
next_char=""

while index < len(s):
    current_idx = index
    string_calc = s[index]
   
    if current_idx >= (len(s)-1):
        print(s[index],string_calc) 
        break
    
    current_char=s[current_idx]
    next_char=s[current_idx+1]
    

    while current_char <= next_char:    
        string_calc = string_calc + next_char 
 
        if current_idx+1 >= (len(s)-1):
            next_char=""
        else:
            current_idx += 1
            current_char=s[current_idx]
            next_char=s[current_idx+1]

        print(s[index],string_calc)         
    if len(string_calc) > len(longest_string):
        longest_string = string_calc
        lenght_longest_string = len(longest_string)
    index += 1

print("Longest substring in alphabetical order is:",longest_string) 
