#declare any imports here for use

# printing hello world and making sure the python compiler work

print("Hello world! Welcome to my program!\n")

# creating a couple recursive funtion to test how variables, functions, if statements, etc are used

def FibonacciRecursive(n):
    if n == 0:
        return 0;
    if n == 1:
        return 1
    return FibonacciRecursive(n - 1) + FibonacciRecursive(n - 2)

# call this when you want to run the fib sequence recursive function.
def FibCaller():
    number = input()
    result = FibonacciRecursive(int(number))
    print(f"The result of the fibonnaci is {result}")

def modifySet(set):
    set.add("Gorilla")
    set.add("Apple") #should not add because it is already in the list
    return set

def modifyDictionary(dictionary, key, value, executions):
    dictionary[key] = value
    #range is pretty helpful if you have a int value that you want to iterate over
    #you can also check if a dictionary has a value in it and conditionaly execute code if it has that value already or insert it possibly with another value if it doesn't
    if key in dictionary:
        for iteration in range(executions):
            dictionary[key] += 1
            print(dictionary[key])

# Note: python is a scripting language by design from what I found and does not need the use of a main function to indicate where to start, it is executed from top to bottom.

# all of these data types are mutable except for tuples which are locked at the set size once created

ex_array = [1, 2, 3, 4, 5] # can be any one type of data
ex_list = ["frog", 3, True] # lists can be any combination of data types and are also
ex_set = {"Apple", "Orange", "Banana", "Lemon"} # can only have one item in this set so if you try to add another apple you will only still get one instance of apple even if you declare it with more than one
ex_dictionary = {
    "isElectric": True,
    "brand": "Ford",
    "model": "Ranger",
    "year": 2003
    }
ex_tuple = ("test", "test2", "test3")
iterations = 5
hashKey = "age"
hashValue = 1


test = modifySet(ex_set)
print(test)

print(ex_list.pop(2))
print("This should remove the  True boolean", ex_list)

ex_array.append("test")
print(ex_array)
#apparently you can add non one types items to an array in python without it modifying it array into a list somehow.

print(ex_dictionary["brand"])

modifyDictionary(ex_dictionary, hashKey, hashValue, iterations) #function to call the modification dictionary that I made to test out how to use them.

print(ex_tuple)
print(len(ex_tuple)) # I seen a bunch of uses of this online where they store the values of a keys for a dictionary in tuples then use them to iterate or find data.
print(ex_tuple.count("test")) # this count looks to be an exact match and not a generalized comparison or contains of whats in the tuple.