# Start writing your functions below this line


def top_half_egg():
    """this creates the top half of the egg"""
    print("  _______")
    print(" /       \\")
    print("/         \\")
def bottom_half_egg():
    """this creates the bottom half of the egg"""
    print("\         /")
    print(" \_______/")
def symbol_line():
    """this creates the crack in the egg"""
    print("-\"-\'-\"-'-\"-")

def chick():
    """this creates a chick"""
    print("   ___")
    print(" ( o >0)")
    print("v(____)v")
    print(" /_  /_")


def main():
    # all of your function calls should go here. Remove the word "pass" before adding function calls.
    pass
    chick()
    top_half_egg()
    bottom_half_egg()
    symbol_line()
    top_half_egg()
    bottom_half_egg()
    symbol_line()
    bottom_half_egg()
    top_half_egg()
    symbol_line()
    bottom_half_egg()
if __name__ == '__main__':
    main()