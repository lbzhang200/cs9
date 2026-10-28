from lab03 import * 

def test_integerDivision():
    assert integerDivision(27, 4) == 6
    assert integerDivision(0, 5) == 0
    assert integerDivision(3, 7) == 0
    assert integerDivision(12, 4) == 3
    assert integerDivision(9, 1) == 9
 
 
def test_collectEvenInts():
    assert collectEvenInts([1, 2, 3, 4, 5]) == [2, 4]
    assert collectEvenInts([]) == []
    assert collectEvenInts([1, 3, 5]) == []
    assert collectEvenInts([2, 4, 6]) == [2, 4, 6]
    assert collectEvenInts([10, 7, 10, 8]) == [10, 10, 8]
 
 
def test_countVowels():
    assert countVowels("This Is A String") == 4
    assert countVowels("") == 0
    assert countVowels("rhythm") == 0
    assert countVowels("AEIOUaeiou") == 10
    assert countVowels("Programming") == 3
 
 
def test_reverseString():
    assert reverseString("CMPSC9") == "9CSPMC"
    assert reverseString("") == ""
    assert reverseString("a") == "a"
    assert reverseString("racecar") == "racecar"
    assert reverseString("ab cd") == "dc ba"
 
 
def test_removeSubString():
    assert removeSubString("Lolololol", "lol") == "Loo"
    assert removeSubString("hello", "xyz") == "hello"
    assert removeSubString("aaaa", "a") == ""
    assert removeSubString("abcabcabc", "abc") == ""
    assert removeSubString("ab", "abc") == "ab"
    assert removeSubString("the cat sat", "at") == "the c s"