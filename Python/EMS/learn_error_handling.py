# try, except, else, finally

while True:
    try:
        a = int(input("Enter two integers:\na: "))
        b = int(input("b: "))
        c = a / b
        break
    # except ValueError:
    #     print("Please enter integers only. Try again!")
    # except ZeroDivisionError:
    #     print("b cannot be zero. Try again...")
    # except:
    #     print("Oops! Something went wrong. Please try again...")
    # except Exception:
    #     print("Oops! Something went wrong. Please try again...")
    except Exception as e:
        print(e, "Try again...")

    else:
        print("This will be printed if there is no exception.")

    finally:
        print("This will be printed no matter what.")
    
    # print("This will be printed no matter what.")


while True:
    op = input("Enter operation (+, -, *, / or x to exit): ").lower()
    if op == "+":
        print(f"{a} + {b} = {a+b}")
    elif op == "-":
        print(f"{a} - {b} = {a-b}")
    elif op == "*":
        print(f"{a} * {b} = {a*b}")
    elif op == "/":
        try:
            print(f"{a} / {b} = {a/b}")
        except ZeroDivisionError:
            print("Sorry! Can't divide by zero, try some other operation...")
    elif op == "x":
        break
    else:
        print("Invalid...")

print("See you soon!")