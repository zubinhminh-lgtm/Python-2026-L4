import math
def ex1():
    r = float(input("Enter circle radius? "))
    print(f"Circle area = {math.pi * r**2:.1f}")
def ex2():
    c = float(input("Enter the temperature in Celsius? "))
    f = c * 9 / 5 + 32
    print(f"{int(c)} (C) = {f:.1f} (F)")
def ex3():
    n = int(input("Enter a number? "))
    is_prime = n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))
    print(f"{n} is {'a prime' if is_prime else 'a NOT prime'} number")
def ex4():
    n = int(input("Enter a number? "))
    is_perfect = n > 0 and sum(i for i in range(1, n) if n % i == 0) == n
    print(f"{n} is {'a perfect' if is_perfect else 'a NOT perfect'} number")
def ex5():
    colors = ["blue", "yellow", "black", "red", "white"]
    color = input("What is your favorite color? ")
    for i in range(0, len(colors)):
        if color.lower() == colors[i]
def ex6():
    print("range1:", list(range(7)))
    print("range2:", list(range(1, 11, 3)))
    print("range3:", list(range(5, 0, -1)))
    print("range4:", list(range(6, -3, -2)))
def remove_dollar_sign(s):
    return s.replace("$", "")
def ex7():
    s = input("Enter string with $: ")
    print("Result:", remove_dollar_sign(s))
def extract_even(l):
    return [x for x in l if x % 2 == 0]
def ex8():
    sample_list = [1, 4, 5, -1, 10]
    print("Evens:", extract_even(sample_list))
def factorial(n):
    return math.factorial(n) if n >= 0 else None
def ex9():
    n = int(input("Enter non-negative integer: "))
    print(f"Factorial of {n} is {factorial(n)}")
def get_divisors(n):
    return [i for i in range(1, n + 1) if n % i == 0]
def ex10():
    n = int(input("Enter a number: "))
    print(f"Divisors of {n}: {get_divisors(n)}")
def ex11():
    x1, y1 = map(float, input("Enter x1, y1: ").split())
    x2, y2 = map(float, input("Enter x2, y2: ").split())
    dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    print(f"Distance = {dist:.2f}")
def print_pattern(m, n):
    for _ in range(m):
        print("* " * n)
def ex12():
    m = int(input("Enter rows (m): "))
    n = int(input("Enter cols (n): "))
    print_pattern(m, n)

if __name__ == "__main__":
    ex1()
