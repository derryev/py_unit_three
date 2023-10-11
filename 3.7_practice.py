

def area_of_a_rectangle(length, height):
    """
    calculates the area of a rectangle
    :param length: length of rectangle entered by the user
    :param height: height of rectangle entered by the user
    :return: the area of the rectanle
    """
    area = length*height
    return area

def main():
    l = 10
    h = 10
    print(area_of_a_rectangle(l,h))
main()