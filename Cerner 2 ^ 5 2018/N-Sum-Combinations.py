# cerner_2^5_2018

# A Python program to print all 3 combinations in a given list that sum up to a given target

from itertools import combinations

s = raw_input("Input the list of numbers seperated by space: ")
numbers = map(int, s.split())
target = input("Enter the target: ")
seqLength = input("Enter the length of the list to be matched: ")
# Get all combinations of the list
# and the specified length
perm = combinations(s, seqLength)
# Check the sum of the generated combinations
for j in list(perm):
    sumList = map(lambda a : int(a), filter(lambda u : u!=' ', j))
    if sum(sumList)==target and len(sumList)==seqLength:
        print j
