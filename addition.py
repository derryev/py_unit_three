# Eva D
# Write your addition function in the space below...
def add_two(number_one, number_two):
    total = number_one+number_two
    print("The sum of",number_one,"and",number_two,"is",total)

def volume_of_cone(radius, height):
    """
    takes parameters for radius and height of a cone and calculates its volume, telling the user either the volume or if
    volume cannot be calculated
    :param radius: the radius of a cone
    :param height: the height of a cone
    :return: nothing
    """
    volume = round(((3.14*radius**2)*(height/3)), 2)
    if height == 0:
        print("The volume of a cone with a height of 0 cannot be calculated")
    else:
        print("The volume of a cone with a radius of",radius,"and a height of",height,"is",volume)


# Do not change anything below these lines
def main():
    pass
    add_two(1,2)
    add_two(3,4)
    add_two(5,6)
    volume_of_cone(24, 3)
if __name__ == '__main__':
    main()