"""An example function definition. """


def my_max(a: int, b: int) -> int:
    """Returns the largest argument."""
    if a>= b:
        return a 
    else:
        return b

print(my_max(10 + 1, 10))
print(my_max(-50, 100))


fortune_luck: int = randint(1, 9)

print("Your fortune cookie says...")

if fortune_luck < 3:
    print("You're amazing person who will recieve good news this week.")
else: 
    if fortune_luck < 5: 
        print("Everyone loves you and is rooting for your success.")
    else:
        if fortune_luck < 7:
        print("You will achieve your dreams just keep fighting.")
         else:
            print("Your story has just begun good things will come.")
