def calculate_area(a, b, c):
    s = (a+b+c/2)
    area = (s*(s-a)*(s-b)*(s-c))**0.5
    return area

def main():
    side_a = 10
    side_b = 20
    side_c = 10
    calculate_area(side_a, side_b, side_c)
    print(calculate_area(side_a, side_b, side_c))



main()

