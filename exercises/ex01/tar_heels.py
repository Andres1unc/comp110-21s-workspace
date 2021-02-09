"""An exercise in remainders and boolean logic."""

__author__ = "730335443"


# Begin your solution here...
Pick_number: int = int(input("Enter an int: "))

if Pick_number % 2 == 0 and Pick_number % 7 == 0:
    print("TAR HEELS")
else: 
    if Pick_number % 2 == 0:
        print("TAR")
    else:
            if Pick_number % 7 ==0:
                print("HEELS")
            else:
                print("CAROLINA")