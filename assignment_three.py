# Eva D
# 10/16/2023
# takes input from user on length, width, and height of a prism to calculate its surface area

def instructions():
    """
    Prints instructions on purpose of and how to use the program to the user.
    return: nothing
    """
    print("Welcome to the total surface area of a rectangular prism calculator!")
    print("This program computes the total surface area of a rectangular prism.")
    print("Please input the length, width, and height of the solid.")

def get_length_input():
    """
    Gets user input on the length of the rectangular prism in the form of a string, converts input to a float.
    :return: The length of the prism as a number(float).
    """
    length = float(input("Please enter the length: "))
    return length

def get_width_input():
    """
    Gets user input on the width of the rectangular prism in the form of a string, converts input to a float.
    :return: The width of the prism as a number (float).
    """
    width = float(input("Please enter the width: "))
    return width

def get_height_input():
    """
    Gets user input on the height of the rectangular prism in the form of a string, converts input to a float.
    :return: The height of the prism as a number(float).
    """
    height = float(input("Please enter the height: "))
    return height

def calc_area(side1, side2):
    """
    Calculates the area of one side of a rectangular prism (a rectangle) using two parameters made up of the length,
    width, or height of the rectangular prism depending on which side's area is being calculated.
    :param side1: One of the side lengths (either width, length, or height) that the user entered (float).
    :param side2: A different side length (either width, length, or height) that the user entered (float).
    :return: The area of one specific side of the rectangular prism based on the lengths used as parameters (float).
    """
    area = side1*side2
    return area

def calc_surface_area_of_prism(length, width, height):
    """
    Calculates the total surface area of the rectangular prism, using the length, width, and height input
    by the user. Uses the calc_area function to find the area of each side and then adds the area of each side of the
    prism together to get total surface area.
    :param length: The length of the prism input by the user (float).
    :param width: The width of the prism input by the user (float).
    :param height: The height of the prism input by the user (float).
    :return: The total surface area of the rectangular prism(float).
    """
    top = calc_area(length, width)
    bottom = calc_area(length, width)
    left_side = calc_area(height, width)
    right_side = calc_area(height, width)
    front = calc_area(height, length)
    back = calc_area(height, length)
    surface_area = top+bottom+left_side+right_side+front+back
    return surface_area

def print_answer(surface_area):
    """
    prints the total surface area of the rectangular prism back to the user with description of what is being printed.
    :param surface_area: the surface area of the prism previously calculated in the calc_surface_area_of_prism function
    (float)
    return: nothing
    """
    print("The surface area of the prism is", surface_area)


def main():
    instructions()
    length = get_length_input()
    width = get_width_input()
    height = get_height_input()
    surface_area = calc_surface_area_of_prism(length, width, height)
    print_answer(surface_area)


main()