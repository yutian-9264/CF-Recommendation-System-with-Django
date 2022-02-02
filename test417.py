def print_numbers(*args):            
    print(type(args))  # tuple
    for n in args:
      print(type(n))   # int

print_numbers(1, 2, 3, 4)
# print(s)