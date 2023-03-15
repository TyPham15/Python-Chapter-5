#Chapter 5 Class Exercise Part 1
def Challenge_1():
    def main():
        texas()
        california()

    def texas():
        birds = int(input('Enter the number of birds: '))
        print(f'Texas has {birds} birds.')

    def california():
        birds = int(input('Enter the number of birds: '))
        print(f'California has {birds} birds.')
    main()
    return str
#commenting the function calls for future usage
#Challenge_1()


def Challenge_2():
    #main function for user input
    def main():
        first_name = input('Enter your first name: ')
        last_name = input('Enter your last name: ')
        address = input('Enter your address: ')
        city = input('Enter your city: ')
        state = input('Enter your state: ')
        zip_code = input('Enter your zip code: ')

        info(first_name, last_name, address, city, state, zip_code)

    #different function to print out the variables
    def info(first, last, address, city, state, zip):
        print(first, last, address, city, state, zip)

    main()
    return str
#Challenge_2()


def Challenge_3():
    
    #main function to ask number
    def main():
        global number
        number = int(input('Enter a number: '))
        show_number()
    #function to print the number
    def show_number():
        print(f'The number you entered is {number}.')

    main()

    #function to add numbers and get total as a return
    def add(num1,num2,num3):
        global total
        total = num1 + num2 + num3
        return total
    add(3,4,5)
    print(total)

    return Challenge_3
#Challenge_3()


def Challenge_4():
   
    #main function to ask for 3 numbers from user
    def main():
        global number
        number1 = int(input('Enter a number: '))
        number2 = int(input('Enter a number: '))
        number3 = int(input('Enter a number: '))
        add(number1, number2, number3)

    #function to add numbers from main
    def add(num1,num2,num3):
        global total
        global average
        total = num1 + num2 + num3
        average = total / 3
        return total, average

    main()
    print(total, average)

    return Challenge_4
#Challenge_4()


def Challenge_5():

    #main function for user input
    def main():
        hours = float(input('Enter the amount of hours worked: '))
        hour_pay = float(input('Enter your hourly pay: '))
        output(hours, hour_pay)

    #function to print out the user input
    def output(hours_worked, hourly_pay):
        print(f'The amount of hours you have worked is {hours_worked} hours.')
        print(f'Your hourly pay for the job is {hourly_pay}.')

    main()
    return Challenge_5
#Challenge_5()