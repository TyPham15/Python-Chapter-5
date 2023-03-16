#Chapter 5 HW

def Project_1():
    #main function to ask for user input
    def main():
        value = float(input('Enter the actual value of the property: '))
        calculate(value)

    #function to calculate the variables as well as print them
    def calculate(value):
        assessment = value * 0.6
        tax = assessment * (0.72 / 100)
        print(f'The assessment value of the property is {assessment}.')
        print(f'The property tax for it is {round(tax, 2)}.')
    
    main()
    return Project_1
#Project_1()


def Project_2():
    #main function to ask user input
    def main():
        class_A = int(input('How many tickets were sold for Class A seats: '))
        class_B = int(input('How many tickets were sold for Class B seats: '))
        class_C = int(input('How many tickets were sold for Class C seats: '))
        calculate(class_A, class_B, class_C)

    #function to calculate total sales
    def calculate(class_A, class_B, class_C):
        total = (class_A * 20) + (class_B * 15) + (class_C * 10)
        print(f'The total for all the ticket sales was ${total}.')

    main()
    return Project_2
#Project_2()


def Project_3():
    #main function to ask user input
    def main():
        total_sales = float(input('Enter the total sales for the month: '))
        calculate(total_sales)

    #function to calculate and print
    def calculate(total):
        state = total * 0.05
        county = total * 0.025
        tax = state + county
        print(f'The state sales tax is ${state}.')
        print(f'The county sales tax is ${county}.')
        print(f'The total sales tax is ${tax}.')

    main()
    return Project_3
#Project_3()