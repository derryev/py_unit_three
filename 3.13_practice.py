



def print_instructions():
    """
    this function takes no parameters and prints out instructions to the user
    :return: none
    """
    print("This program converts Fahrenheit to Celsius")
    print("Please enter a temperature in Fahrenheit")

def get_user_input():
    """takes no parameters, returns the temperature as a float, gets input from the user"""
    fahrenheit = input("Enter Temp: ")
    return float(fahrenheit)

def convert_f_to_c(temperature):
    """
    this function converts Fahrenheit temperature to temperature in Celsius
    :param temperature:
    :return: Celsius as a float
    """
    celsius = 5/9*(temperature-32)
    return celsius

def print_result(result):
    """
    prints the result of the calculations
    :param result:
    :return: nothing
    """
    print("The temperature in celsius is",result)

def main():
   print_instructions()
   temperature = get_user_input()
   result = convert_f_to_c(temperature)
   print_result(result)




main()