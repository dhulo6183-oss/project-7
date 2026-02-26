import datetime
import math
import random
import uuid
import os
import time
import string


while True:
    print("\n==============================")
    print("Welcome to Multi-Utility Toolkit")
    print("==============================")
    print("1. Datetime and Time Operations")
    print("2. Mathematical Operations")
    print("3. Random Data Generation")
    print("4. Generate Unique Identifiers (UUID)")
    print("5. File Operations")
    print("6. Explore Module Attributes (dir())")
    print("7. Exit")

    choice = input("Enter your choice: ")

    # =========================
    # Datetime Operations
    # =========================
    if choice == "1":
        print("\n1. Current Date & Time")
        print("2. Date Difference")
        print("3. Format Date")
        print("4. Stopwatch")
        print("5. Countdown")
        sub = input("Enter choice: ")

        if sub == "1":
            print("Current Date & Time:", datetime.datetime.now())

        elif sub == "2":
            d1 = input("Enter first date (YYYY-MM-DD): ")
            d2 = input("Enter second date (YYYY-MM-DD): ")
            date1 = datetime.datetime.strptime(d1, "%Y-%m-%d")
            date2 = datetime.datetime.strptime(d2, "%Y-%m-%d")
            print("Difference:", abs((date2 - date1).days), "days")

        elif sub == "3":
            d = input("Enter date (YYYY-MM-DD): ")
            date = datetime.datetime.strptime(d, "%Y-%m-%d")
            print("Formatted:", date.strftime("%d-%m-%Y"))

        elif sub == "4":
            input("Press Enter to start...")
            start = time.time()
            input("Press Enter to stop...")
            end = time.time()
            print("Time:", round(end - start, 2), "seconds")

        elif sub == "5":
            sec = int(input("Enter seconds: "))
            while sec > 0:
                print("Time left:", sec)
                time.sleep(1)
                sec -= 1
            print("Time's up!")

    # =========================
    # Mathematical Operations
    # =========================
    elif choice == "2":
        print("\n1. Factorial")
        print("2. Compound Interest")
        print("3. Trigonometry")
        print("4. Area")
        sub = input("Enter choice: ")

        if sub == "1":
            num = int(input("Enter number: "))
            print("Factorial:", math.factorial(num))

        elif sub == "2":
            p = float(input("Principal: "))
            r = float(input("Rate (%): "))
            t = float(input("Time (years): "))
            amount = p * (1 + r/100) ** t
            print("Amount:", round(amount, 2))

        elif sub == "3":
            angle = float(input("Enter angle in degrees: "))
            rad = math.radians(angle)
            print("Sin:", math.sin(rad))
            print("Cos:", math.cos(rad))
            print("Tan:", math.tan(rad))

        elif sub == "4":
            print("1. Circle")
            print("2. Rectangle")
            shape = input("Choose: ")

            if shape == "1":
                r = float(input("Radius: "))
                print("Area:", math.pi * r * r)
            elif shape == "2":
                l = float(input("Length: "))
                w = float(input("Width: "))
                print("Area:", l * w)

    # =========================
    # Random Data
    # =========================
    elif choice == "3":
        print("\n1. Random Number")
        print("2. Random List")
        print("3. Random Password")
        print("4. Random OTP")
        sub = input("Enter choice: ")

        if sub == "1":
            print("Random Number:", random.randint(1, 100))

        elif sub == "2":
            lst = [random.randint(1, 50) for _ in range(5)]
            print("Random List:", lst)

        elif sub == "3":
            length = int(input("Password length: "))
            chars = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(random.choice(chars) for _ in range(length))
            print("Password:", password)

        elif sub == "4":
            print("OTP:", random.randint(100000, 999999))

    # =========================
    # UUID
    # =========================
    elif choice == "4":
        print("Generated UUID:", uuid.uuid4())

    # =========================
    # File Operations
    # =========================
    elif choice == "5":
        print("\n1. Create File")
        print("2. Write File")
        print("3. Read File")
        print("4. Append File")
        sub = input("Enter choice: ")

        if sub == "1":
            name = input("File name: ")
            open(name, "w").close()
            print("File created!")

        elif sub == "2":
            name = input("File name: ")
            data = input("Enter data: ")
            with open(name, "w") as f:
                f.write(data)
            print("Written successfully!")

        elif sub == "3":
            name = input("File name: ")
            if os.path.exists(name):
                with open(name, "r") as f:
                    print(f.read())
            else:
                print("File not found!")

        elif sub == "4":
            name = input("File name: ")
            data = input("Enter data: ")
            with open(name, "a") as f:
                f.write("\n" + data)
            print("Appended successfully!")

    # =========================
    # Explore Module
    # =========================
    elif choice == "6":
        module_name = input("Enter module name: ")
        try:
            module = _import_(module_name)
            print(dir(module))
        except:
            print("Module not found!")

    # =========================
    # Exit
    # =========================
    elif choice == "7":
        print("Thank you for using the Multi-Utility Toolkit!")
        break

    else:
        print("Invalid choice!")
