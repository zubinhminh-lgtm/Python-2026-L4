[Lab1_2510712_Vũ Bình Minh.py](https://github.com/user-attachments/files/32529033/Lab1_2510712_Vu.Binh.Minh.py)
USTH Advanced Programming with Python 2026
==================================

*Vũ Bình Minh
*2510712
[Uploading Lab1_2510712_Vũ Bình Minh.py…]()
#Lab lesson 1: Python Basics
#1
import math
r = float(input("Enter circle radius:"))
area = math.pi * r**2
print(f"Circle area = {area}")
#2
c = float(input("Enter temperature in Celsius:"))
f = (c * 9 / 5) + 32
print(f"{c} (C) = {f} (F)")
#3
n = int(input("Enter a number:"))
if n < 2:
    notprime = False
else:
    prime = all(n % i != 0 for i in range(2, int(n**0.5) + 1))
if prime:
    print(f"{n} is a prime number")
else:
    print(f"{n} is a NOT prime number")
#4
n = int(input("Enter a number:"))
if n > 0 and sum(i for i in range(1, n) if n % i == 0) == n:
    print(f"{n} is a perfect number")
else:
    print(f"{n} is a NOT perfect number")
#5
colors = ["Blue", "Yellow", "Black", "Red", "White"]
your_color = input("What is your favorite color:")
if your_color in colors:
    print(f"Your color is in index {colors.index(your_color)} in my list")
else:
    print("Sorry, I could not find your color")
#6
print("range1 |", list(range(7)))
print("range2 |", list(range(1, 11, 3)))
print("range3 |", list(range(5, 0, -1)))
print("range4 |", list(range(6, -3, -2)))
#7
def remove_dollar_sign(s):
    return s.replace("$", "")
#8
def extract_even(l):
    return [x for x in l if x % 2 == 0]
#9
def factorial(n):
    if n < 0:
        return None
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
#10
def get_divisors(n):
    return [i for i in range(1, abs(n) + 1) if n % i == 0]
#11
import math
x1, y1 = map(float, input("Enter x1, y1: ").split())
x2, y2 = map(float, input("Enter x2, y2: ").split())
distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print(f"Distance: {distance}")
#12
def print_pattern(m, n):
    for _ in range(m):
        print("*" * n)
