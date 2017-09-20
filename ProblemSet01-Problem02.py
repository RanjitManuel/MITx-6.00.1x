"""
Problem 2
10.0/10.0 points (graded)
Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2

"""
s = 'azcbobobegghakl'

BobCount = 0
index = 0

while index < len(s):
    index_3 = index + 3
    if s[index:index_3] == "bob":
        BobCount += 1
    index += 1

print("Number of times bob occurs is:", BobCount)
