# 1. Write a Python function to sort a dictionary by value.

my_dict = {"mango": 15, "apple": 120, "peas": 90, "kiwi": 300, "avocado": 30}
fruits = sorted(my_dict.items(), key=lambda a:a[1], reverse=True)
print(fruits)


# 2. Write a Python program to find the second largest value in a dictionary.

def value (second):
    a = second.values()
    b = sorted(a)
    c = b[-2]
    print(c)

ans = {"eggs": 100, "milk": 200, "delmonte":120, "yoghurt": 500}    
value(ans)

# 3. Write a Python program to find the sum of all values in a dictionary.

def sums(value):
    return sum(value.values())

value = {"a":2, "d":1, "z":10, "t":5}
print(sums(value))


# 4. Write a Python program to convert a dictionary to a list of tuples.

view_dict = {"clarah": 27, "ambrose": 24, "issabella": 23, "vince": 20}
my_tuple = list(view_dict.items())
print(my_tuple)


# 5. Write a Python function to merge two dictionaries into one. 

def merge(dict1, dict2):
    return (dict2.update(dict1))

dict1 = {"c": 2, "d": 4, "v": 1}
dict2 = {"w":5, "a":6}

print(merge(dict1,dict2))
print(dict2)

#                               TAKEAWAY KEYS

# 1. Dictionaries store key-value pairs using curly braces {}

# 2. Values are accessed using keys inside square brackets []

# 3. You can add or modify key-value pairs using assignment (=)

# 4. Iteration can be done using the keys(), values(), and items() methods








