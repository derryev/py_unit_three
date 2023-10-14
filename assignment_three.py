# Eva D
# October {} 2023
# takes input from user on length, width, and height of a prism to calculate its surface area

def instructions():
    print("Welcome to the total surface area of a rectangular prism calculator!")
    print("This program computes the total surface area of a rectangular prism.")
    print("Please input the length, width, and height of the solid.")

def get_length_input():
    length = float(input("Please enter the length: "))
    return length

def get_width_input():
    width = float(input("Please enter the width: "))
    return width

def get_height_input():
    height = float(input("Please enter the height: "))
    return height

def calc_area(side1, side2):
    area = side1*side2
    return area

def calc_surface_area_of_prism(length, width, height):
    top = calc_area(length, width)
    bottom = calc_area(length, width)
    left_side = calc_area(height, width)
    right_side = calc_area(height, width)
    front = calc_area(height, length)
    back = calc_area(height, length)
    surface_area = top+bottom+left_side+right_side+front+back
    return surface_area

def print_answer(surface_area):
    print("The surface area of the prism is", surface_area)


def main():
    instructions()
    length = get_length_input()
    width = get_width_input()
    height = get_height_input()
    surface_area = calc_surface_area_of_prism(length, width, height)
    print_answer(surface_area)


main()