def main ():
    while(input('Do you want to use calculator? y/n \n')=='y'):
        a = float(input('Provide me first number\n'))
        operator = input('Provide me an operator\n')
        b = float(input('Provide me second number\n'))
        if operator == '+':
            a = a + b
        if operator == '-':
            a = a - b
        if operator == '*':
            a = a * b
        if operator == '/':
            a = a / b
        print(f"Result: {a}")

if __name__ == "__main__":
    main()