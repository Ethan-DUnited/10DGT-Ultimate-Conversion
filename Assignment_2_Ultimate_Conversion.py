# Ultimate Conversion Calculator
# Author: Ethan du Toit
# Version: V1.0

# VALUE DICTIONARIES - references back to these dictionaries when user asks to convert values
# 1️⃣ Distance Dictionary
distance_dict = {
    "mm": 1000,
    "cm": 100,
    "m": 1,
    "km": 0.001
}

# 2️⃣ Mass Dictionary
mass_dict = {
    "mg": 1000000,
    "g": 1000,
    "kg": 1,
    "t": 0.001
}

# 3️⃣ Time Dictionary
time_dict = {
    "ms": 3600000,
    "s": 3600,
    "min": 60,
    "hr": 1,
    "day": 0.04166667,
    "week": 0.00595238,
    "month": 0.0014881,
    "yr": 0.00012401
}

# 4️⃣ Volume Dictionary
volume_dict = {
    "ml": 1000,
    "l": 1,
    "kL": 0.001,
    "mL": 0.000001
}


def inputvalue(message):
    while True:
        try:
            userInput = int(input(message))
            if userInput > 0:
                done = True
            else:
                print(integererror)
        except ValueError:
            print(integererror)

print("\n🎉 WELCOME TO THE ULTIMATE CONVERSION CALCULATOR! 🎉")

keep_going = ""
while keep_going == "":

    
    done = False
    error = "Please enter a valid conversion type "
    integererror = "Please enter a valid number "
    while not done:
        conversion_type = str(input("\nPlease enter the conversion type that you wish to complete.\nAcceptable conversion types:\n- 🧭 'distance'\n- 🏋️‍♂️ 'mass'\n- ⏰ 'time'\n- 🍾 'volume'\n\nCONVERSION TYPE: ").lower())
        if conversion_type == "distance":
            # Distance conversion
            
            amount = inputvalue("\nHow much? ")

            from_unit = input("From Unit? ")
            if from_unit == "mm" or from_unit == "cm" or from_unit == "m" or from_unit == "km":
                continue
            else:
                print(error)

            to_unit = input("To Unit? ")
            if to_unit == "mm" or to_unit == "cm" or to_unit == "m" or to_unit == "km":
                continue
            else:
                print(error)
            
            multiply_by = distance_dict[to_unit]/distance_dict[from_unit]
            standard = amount * multiply_by
            done = True

        elif conversion_type == "mass":
            # Mass conversion
            amount = float(input("\nHow much? "))
            from_unit = input("From Unit? ")
            to_unit = input("To Unit? ")

            multiply_by = mass_dict[to_unit]/mass_dict[from_unit]
            standard = amount * multiply_by
            done = True

        elif conversion_type == "time":
            # Mass conversion
            amount = float(input("\nHow much? "))
            from_unit = input("From Unit? ")
            to_unit = input("To Unit? ")

            multiply_by = time_dict[to_unit]/time_dict[from_unit]
            standard = amount * multiply_by
            done = True

        elif conversion_type == "volume":
            # Mass conversion
            amount = float(input("\nHow much? "))
            from_unit = input("From Unit? ")
            to_unit = input("To Unit? ")

            multiply_by = volume_dict[to_unit]/volume_dict[from_unit]
            standard = amount * multiply_by
            done = True

        else:
            print(error)
            
    print(f"There are {standard} {to_unit} in {amount} {from_unit}\n")
    keep_going = input("Press enter to complete another calculation, or any other key to end the program. ") # Loops program if requested



# Get amount and units (we assume they are valid)



# Multiply to get to our standard value





# Divide to get to desired value
# divide_by = distance_dict[from_unit]
# answer = standard / divide_by





