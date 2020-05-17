# Week 2 Assignment
# Q1. Create a function with name findMaxMin, that will accept variable(any number of arguments) arguments and
# print the following:
# 1. Number of arguments passed
# 2. max and min value of arguments
# 3. Sum of the values of the arguments

from pip._vendor.distlib.compat import raw_input
if __name__ == "__main__":
    # read arguments from user input
    args = raw_input("Enter arguments separated by space: ")
    # validate input if all inputs are numeric or not and quit if not all are numeric
    for arg in args.split(" "):
        if not(arg.isnumeric()):
            print("Invalid input {}! Only numeric should be given".format(arg))
            quit()
# split the input and use list comprehension to create list
arglist = [int(i) for i in args.split(" ")]
print("Number of arguments: {}".format(len(arglist)))
print("Maximum and minimum value: {} and {} respectively".format(max(arglist), min(arglist)))
print("Sum of the arguments: {}".format(sum(arglist)))