# Write countWords(s) that takes a string of words separated by spaces and returns a dictionary mapping each word 
# (lowercased) to how many times it appears. countWords("The cat the Dog") returns {"the": 2, "cat": 1, "dog": 1}.

def countWords(s): 
    count = {}
    for word in s.lower().split():
        if word in count:
            count[word] = count.get(word, 0) + 1
        else:
            count[word] = 1
    return count 

"""
Write safeDivide(a, b) that:
• returns a / b normally
• returns None if b is 0
• raises a ValueError with the message "numbers only" if a or b isn't a number (catch the TypeError that division raises)
"""

def safeDivide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None
    except TypeError:
        raise ValueError("numbers only")



 """
 5.3 Classes: BankAccount
Write a class BankAccount with:
• a constructor taking owner (string) and balance (default 0)
• deposit(amount): raises ValueError if amount <= 0, otherwise adds it
• withdraw(amount): raises ValueError if amount is more than the balance, otherwise subtracts it
• __str__ returning "<owner>: $<balance>", like "Leo: $50"
• __eq__ that's True when owner and balance both match
• __le__ that compares balances
5.4 Inheritance: SavingsAccount
Write SavingsAccount, a subclass of BankAccount:
• its constructor also takes rate (like 0.05) and must call the parent constructor
• addInterest() adds balance * rate to the balance
• it overrides withdraw(amount) so the balance can never go below 100 (raise ValueError if it would), then uses the parent's withdraw to do the actual subtraction
 """

class BankAccount:
    def __init__(self, owner, balance=0)
        self.owner = owner 
        self.balance = balance 

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("deposit must be positive")
        self.balance += amount 

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("amount cannot be more than the balance")
        self.balance -= amount 

    def __str__(self):
        return "{}: ${}".format(self.name, self.balance)

    def __eq__(self, other):
        if self.owner == other.owner and self.balance == other.balance: 
            return True 

    def __le__(self, other):
        return self.balance <= other.balance 


from BankAccount import BankAccount

class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, rate=0.05):
        super().__init__(owner, balance)
        self.rate = rate 

    def addInterest(self):
        self.balance += self.balance * self.rate 

    def withdraw(self, amount):
        if self.balance - amount < 100:
            raise ValueError("balance can never go below 100")
        super().withdraw(amount)
    
"""
5.5 Recursion
Write each of these recursively, with no loops:
1. sumList(lst): returns the sum of a list of numbers. sumList([]) is 0.
2. countChar(s, c): returns how many times character c appears in string s.
3. reverse(s): returns the string reversed.
4. power(base, exp): returns base to the power exp, for exp ≥ 0.
"""
def sumList(lst):
    if len(lst) == 0:
        return 0
    return lst[0] + sumList[lst[1:]]

def countChar(s, c):
    if s == "":
        return 0 
    if s[0] == c:
        return 1 + countChar(s[1:], c)
    return countChar(s[1:], c)

def reverse(s):
    if len(s) <= 1:
        return s 
    return reverse(s[1:]) + s[0]

def power(base, exp):
    if exp == 0:
        return 1 
    return base * power(base, exp - 1)




"""
5.6 Stack application: balanced brackets
Using the lecture Stack class, write isBalanced(s) that returns True if every (, [ and { in s is closed in the right order. isBalanced("{[()]}") is True; isBalanced("([)]") and isBalanced("((") are False.
""" 

def isBalanced(s):
    pairs = {")":"(", "]":"[", "}": "{"}

    stack = []
    for ch in s:
        if ch in "{[(":
            stack.push(ch)
        elif ch in pairs:
            if stack.isEmpty() or stack.pop() != pairs[ch]: #if top of stack doesn't contain the other half shown in pairs 
                return False 
    return stack.isEmpty()


"""
5.7 Deque application: palindrome check
Using the lecture Deque class, write isPalindrome(s) that returns True if s reads the same forwards and backwards.
"""

def isPalindrome(s):
    d = Deque() 
    for ch in s:
        d.addRear(ch)
    while d.size() > 1:
        if d.removeFront() != d.removeRear(): #fron is left side, rear is right side) 
            return False 
    return True 


"""
5.8 Testing with pytest
Write pytest test functions for BankAccount from 5.3. Cover: a normal deposit, a withdraw that's too big (it should raise ValueError), and __eq__ on two equal accounts.

"""

import pytest: 

def test_deposit(): 
    


