# cerner_2^5_2018

# Given a string a, find the longest palindromic substring contained in a.
def isPalindrome(s):
    if not s:
        return False
    return s == s[::-1]
    
def longestPalindromicSubstring(s):
    if not s:
        return ""

    n = len(s)
    longest, left, right = 0, 0, 0
    for i in range(0, n):
        for j in range(i + 1, n + 1):
            substr = s[i:j]
            if isPalindrome(substr) and len(substr) > longest:
                longest = len(substr)
                left, right = i, j
    result = s[left:right]
    return result

def main():
    s = input("Enter a string:")
    print (longestPalindromicSubstring(s))

if __name__ == '__main__':
    main()