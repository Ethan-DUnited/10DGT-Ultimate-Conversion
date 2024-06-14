# Ultimate Conversion Calculator
# Author: Ethan du Toit
# Version: V3.7

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


print("\n🎉 WELCOME TO THE ULTIMATE CONVERSION CALCULATOR! 🎉") # Welcomes user to program

keep_going = ""
keep_going = input("Press <ENTER> ⏎ to continue, or any other key to end the program. ") # Keep going loop gives the user the option to quit the program if they don't wish to continue anymore

while keep_going == "": # While loop - used at the end if user wants to repeat program another time.
    
    done = False

    # Error messages - shown to user if they enter an invalid value
    error = "⛔️ Please enter a valid conversion type ⛔️"
    integererror = "⛔️ Please enter a valid number (integer must be higher than zero) ⛔️"

    # Valid input checker function - used to make sure user enters the correct conversion values, otherwise shows error.
    def get_valid_input(prompt, valid_values):
        while True:
            user_input = input(prompt)
            if user_input in valid_values:
                return user_input
            else:
                print(error)

    # Asks user which conversion type they would like and gives acceptable values
    while not done:
        conversion_type = str(input("\nPlease enter the conversion type that you wish to complete.\nAcceptable conversion types are listed below (case sensitive):\n- 🧭 'distance'\n- 🏋️‍♂️ 'mass'\n- ⏰ 'time'\n- 🍾 'volume'\n\nCONVERSION TYPE? ").lower())

        # 🧭 DISTANCE CONVERSION CALCULATOR - user enters amount & the from and to units. Program then converts and gives output at end of program
        if conversion_type == "distance":
            while True:
                try:
                    amount = float(input("\nHow much? "))
                    if amount > 0:
                        break # Exits loop if valid number is provided
                    else:
                        print(integererror)
                except ValueError:
                    print(integererror) 
        
            # Asks user to input their "to" and "from" values
            from_unit = get_valid_input("\nAcceptable distance unit types are listed below: (case sensitive)\n1. mm\n2. cm\n3. m\n4. km\n\nFrom Unit? ", ["mm","cm","m","km"])
            print()
            to_unit = get_valid_input("\nAcceptable distance unit types are listed below: (case sensitive)\n1. mm\n2. cm\n3. m\n4. km\n\nTo Unit? ", ["mm","cm","m","km"])
            
            # Completes calculation, referencing back to dictionary
            multiply_by = distance_dict[to_unit]/distance_dict[from_unit]
            standard = amount * multiply_by
            done = True
           
        
        # 🏋️‍♂️ MASS CONVERSION CALCULATOR - user enters amount & the from and to units. Program then converts and gives output at end of program
        elif conversion_type == "mass":
            while True:
                try:
                    amount = float(input("\nHow much? "))
                    if amount > 0:
                        break # Exits loop if valid number is provided
                    else:
                        print(integererror)
                except ValueError:
                    print(integererror)  

            # Asks user to input their "to" and "from" values
            from_unit = get_valid_input("Acceptable mass unit types are listed below: (case sensitive)\n1. mg\n2. g\n3. kg\n4. t\n\nFrom Unit? ", ["mg","g","kg","t"])
            print()
            to_unit = get_valid_input("Acceptable mass unit types are listed below: (case sensitive)\n1. mg\n2. g\n3. kg\n4. t\n\nTo Unit? ", ["mg","g","kg","t"])

            # Completes calculation, referencing back to dictionary
            multiply_by = mass_dict[to_unit]/mass_dict[from_unit]
            standard = amount * multiply_by
            done = True

        # ⏰ TIME CONVERSION CALCULATOR - user enters amount & the from and to units. Program then converts and gives output at end of program
        elif conversion_type == "time":
            while True:
                try:
                    amount = float(input("\nHow much? "))
                    if amount > 0:
                        break # Exits loop if valid number is provided
                    else:
                        print(integererror)
                except ValueError:
                    print(integererror)

            # Asks user to input their "to" and "from" values
            from_unit = get_valid_input("Acceptable time unit types are listed below: (case sensitive)\n1. ms\n2. s\n3. min\n4. hr\n5. day\n6. week\n7. month\n8. yr\n\nFrom Unit? ", ["ms","s","min","hr","day","week","month","yr"])
            print()
            to_unit = get_valid_input("Acceptable time unit types are listed below: (case sensitive)\n1. ms\n2. s\n3. min\n4. hr\n5. day\n6. week\n7. month\n8. yr\n\nTo Unit? ", ["ms","s","min","hr","day","week","month","yr"])

            # Completes calculation, referencing back to dictionary
            multiply_by = time_dict[to_unit]/time_dict[from_unit]
            standard = amount * multiply_by
            done = True

        # 🍾 VOLUME CONVERSION CALCULATOR - user enters amount & the from and to units. Program then converts and gives output at end of program
        elif conversion_type == "volume":
            while True:
                try:
                    amount = float(input("\nHow much? "))
                    if amount > 0:
                        break # Exits loop if valid number is provided
                    else:
                        print(integererror)
                except ValueError:
                    print(integererror)

            # Asks user to input their "to" and "from" values
            from_unit = get_valid_input("Acceptable volume unit types are listed below: (case sensitive)\n1. ml\n2. l\n3. kL\n4. mL\n\nFrom Unit? ", ["ml","l","kL","mL"])
            print()
            to_unit = get_valid_input("Acceptable volume unit types are listed below: (case sensitive)\n1. ml\n2. l\n3. kL\n4. mL\n\nTo Unit? ", ["ml","l","kL","mL"])

            # Completes calculation, referencing back to dictionary
            multiply_by = volume_dict[to_unit]/volume_dict[from_unit]
            standard = amount * multiply_by
            done = True

        # IF USER ENTERS ANYTHING OTHER THAN SPECIFIED CONVERSION TYPES, ERROR MESSAGE SHOWS AND PROMPT REPEATS.
        else:
            print(error)

    # Program takes result and prints it out for user to see converted value.      
    print(f"\n----------\n🔑 RESULT: There are {standard}{to_unit} in {amount}{from_unit}\n")

    # LOOPS PROGRAM AGAIN IF REQUESTED (uses while loop in lines 44-46)
    keep_going = input("Press ENTER ⏎ to complete another calculation, or any other key to end the program. ")

print("----------\n\nTHANK YOU FOR USING THE ULTIMATE CONVERSION CALCULATOR! 🚀\n")