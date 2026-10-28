def integerDivision(n, k):
    if n < k:
        return 0
    return 1 + integerDivision(n - k, k)

def collectEvenInts(listOfInt):
    if listOfInt == []:
        return []
    if listOfInt[0] % 2 == 0:
        return [listOfInt[0]] + collectEvenInts(listOfInt[1:])
    return collectEvenInts(listOfInt[1:])

def countVowels(someString):
    if someString == "":
        return 0
    if someString[0] in "AEIOUaeiou":
        return 1 + countVowels(someString[1:])
    return countVowels(someString[1:])


def reverseString(s):
    if s == "": 
        return ""
    return reverseString(s[1:]) + s[0]

def removeSubString(s, sub): 
    if len(s) < len(sub):
        return s
    if s[0:len(sub)] == sub: 
        return removeSubString(s[len(sub):], sub)
    return s[0] + removeSubString(s[1:], sub)
