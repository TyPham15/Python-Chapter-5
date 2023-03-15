#Chapter 5 Class Exercise Part 2
def Challenge_1():

    #main function to ask for distance
    def main():
        distance = float(input('Enter a distance in kilometers: '))
        calculate(distance)

    #function to calculate the distance to miles
    def calculate(kilometers):
        miles = kilometers * 0.6214
        print(f'The distance in miles is {miles}.')

    main()
    return Challenge_1
#Challenge_1()


def Challenge_2():

    #main function for user input first
    def main():
        loan = float(input('Enter the monthly costs of the loan: '))
        insurance = float(input('Enter the monthly costs of the insurance: '))
        gas = float(input('Enter the monthly costs of the gas: '))
        oil = float(input('Enter the monthly costs of the oil: '))
        tires = float(input('Enter the monthly costs of the tires: '))
        maintenance = float(input('Enter the monthly costs of the maintenance: '))
        calculate(loan, insurance, gas, oil, tires, maintenance)

    #function to calculate all annual payments
    def calculate(loan, insurance, gas, oil, tires, maintenance):

        annual_loan = loan * 12
        annual_insurance = insurance * 12
        annual_gas = gas * 12
        annual_oil = oil * 12
        annual_tires = tires * 12
        annual_maintenance = maintenance * 12
        
        output(annual_loan, annual_insurance, annual_gas, annual_oil, annual_tires, annual_maintenance)

    #function to print out all annual payments
    def output(loan, insurance, gas, oil, tires, maintenance):
        print(f'The total annual cost of loans is {loan}.')
        print(f'The total annual cost of insurance is {insurance}.')
        print(f'The total annual cost of gas is {gas}.')
        print(f'The total annual cost of oil is {oil}.')
        print(f'The total annual cost of tires is {tires}.')
        print(f'The total annual cost of maintenance is {maintenance}.')

    main()
    return Challenge_2
#Challenge_2()