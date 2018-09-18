# cerner_2^5_2018

# Given two strings a and b, determine whether some anagram of b is a substring of a

def is_anagram(s1, s2):
    s1 = list(s1)
    s1.sort()  
    return s1 == s2

def anagram(s, t):
    match_length = len(t)
    pattern_length = len(s)
    sorted_t = list(t)
    sorted_t.sort()      
    for i in range(pattern_length - match_length + 1):
        if is_anagram(s[i: i+match_length], sorted_t):
            return True
    return False

def main():
    string1 = input("Enter the first string:")
    string2 = input("Enter the second string:")
    print (anagram(string1, string2));

if __name__ == '__main__':
    main()