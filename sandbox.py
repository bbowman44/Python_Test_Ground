# printing hello world and making sure the python compiler work

print("Hello world! Welcome to my program!\n")

# creating a couple recursive funtion to test how variables, functions, if statements, etc are used

def FibonacciRecursive(n):
    if n == 0:
        return 0;
    if n == 1:
        return 1
    return FibonacciRecursive(n - 1) + FibonacciRecursive(n - 2)

number = input()
result = FibonacciRecursive(int(number))
print(f"The result of the fibonnaci is {result}")

# Note: python is a scripting language by design from what I found and does not need the use of a main function to indicate where to start, it is executed from top to bottom.

