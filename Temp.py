import math
from decimal import Decimal

print("Welcome to this temperture calcuator")
while True:
    print("Please choose from which unit you want to convert")
    print("Type A for 'Kelvin'")
    print("Type B for 'Celsius'")
    print("Type C for 'Fahrenheit'")
    print("Or type Q to quit")

    From_Temp = input(">>> ").upper()
    if From_Temp not in ['A', 'B', 'C', 'Q']:
        print("Invalid Choice, Please try again")
        continue
    if From_Temp == "Q":
        print("Quiting program..")
        exit()
    if From_Temp == "A":
        print("Please enter the Kelvin value below")
        
        Kelvin_Val = float(input(">>> "))
        unit_A = "K"

        print("To what do you want to convert?")
        print("Type A for 'Celsius'")
        print("Type B for 'Fahrenheit")

        To_what = input(">>> ").upper()
        if To_what not in ['A', 'B']:
            print("Invalid choice, Please try again")
            continue
        elif To_what == "A":
            Kelvin_Celcius = round(Kelvin_Val - 273.15)
            unit_B = "C"

            output_A = f"{Kelvin_Val} {unit_A}"
            output_B = f"{Kelvin_Celcius} {unit_B}"
            final_output = f"{output_A} = {output_B}"

            print(final_output)

        elif To_what == "B":
            Kelvin_Fahrenheit = round((Kelvin_Val - 273.15) * 9/5 + 32)
            unit_B = "F"

            output_A = f"{Kelvin_Val} {unit_A}"
            output_B = f"{Kelvin_Fahrenheit} {unit_B}"
            final_output = f"{output_A} = {output_B}"

            print(final_output)

    elif From_Temp == "B":
        print("Please enter the Celsius value below")

        Celsius_Val = float(input(">>> "))
        unit_A = "C"

        print("To what do you want to convert?")
        print("Type A for 'Kelvin'")
        print("Type B for 'Fahrenheit")

        To_what = input(">>> ").upper()
        if To_what not in ['A', 'B']:
            print("Invalid Choice, Please try again")
            continue
        elif To_what == "A":
            Celsius_Kelvin = round(Celsius_Val + 273.15)
            unit_B = "K"

            output_A = f"{Celsius_Val} {unit_A}"
            output_B = f"{Celsius_Kelvin} {unit_B}"
            final_output = f"{output_A} = {output_B}"

            print(final_output)

        elif To_what == "B":
            Celsius_Fahrenheit = round((Celsius_Val * 9/5) + 32)
            unit_B = "F"

            output_A = f"{Celsius_Val} {unit_A}"
            output_B = f"{Celsius_Fahrenheit} {unit_B}"
            final_output = f"{output_A} = {output_B}"

            print(final_output)

    elif From_Temp == "C":
        print("Please enter the Fahrenheit value below")

        Fahrenheit_Val = float(input(">>> "))
        unit_A = "F"

        print("To what do you want to convert?")
        print("Type A for 'Kelvin'")
        print("Type B for 'Celsius")

        To_what = input(">>> ").upper()
        if To_what not in ['A', 'B']:
            print("Invalid Choice, Please try again")
            continue
        elif To_what == "A":
            Fahrenheit_Kelvin = round((Fahrenheit_Val - 32) * 5/9 + 273.15)
            unit_B = "K"

            output_A = f"{Fahrenheit_Val} {unit_A}"
            output_B = f"{Fahrenheit_Kelvin} {unit_B}"
            final_output = f"{output_A} = {output_B}"

            print(final_output)

        elif To_what == "B":
            Fahrenheit_Celsius = round((Fahrenheit_Val - 32) * 5/9)
            unit_B = "C"

            output_A = f"{Fahrenheit_Val} {unit_A}"
            output_B = f"{Fahrenheit_Celsius} {unit_B}"
            final_output = f"{output_A} = {output_B}"

            print(final_output)