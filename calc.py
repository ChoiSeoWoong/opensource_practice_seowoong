def plus(x, y):
    return x+y

def minus(x, y):
    return x-y

def multiply(x, y):
    return x*y

def divide(x, y):
    return x/y

# main function
def main():
    check = 1
    print("Welcome to calculator")
    while check >= 1:        
        print("0: exit, 1: plus, 2: minus, 3: multiply, 4: divide")
        check_input = input()
        try:
            check = int(check_input)
            if check == 1:
                print("First Number")
                x = float(input())
                print("Second Number")
                y = float(input())

                result = round(plus(x, y), 2)
                print("answer : ", result)

            elif check == 2:
                print("First Number")
                x = float(input())
                print("Second Number")
                y = float(input())
                
                result = round(minus(x, y), 2)
                print("answer : ", result)

            elif check == 3:
                print("First Number")
                x = float(input())
                print("Second Number")
                y = float(input())
                
                result = round(multiply(x, y), 2)
                print("answer : ", result)

            elif check == 4:
                print("First Number")
                x = float(input())
                print("Second Number")
                y = float(input())
                
                result = round(divide(x, y), 2)
                print("answer : ", result)

            elif check == 0:
                print("Thank you")

            else:
                print("Unsupported operation")
                print("Please try again")
        
        except ValueError:
            print("Please try again")
            continue

if __name__ == "__main__":
    main()
