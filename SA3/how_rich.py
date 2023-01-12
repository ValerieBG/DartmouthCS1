# filename: how_rich.py
# author:   Valerie Gadapati
# date:     Jan 11, 2023
# purpose:  computes Brutus's current wealth starting with $1.00 after 5% interest is compounded 2021 times

# define some variables about the investment
BRUTUS_INITAL_INVESTMENT = 1.00
BRUTUS_INTEREST_RATE = 0.05
start_year = 0

# function to calculate an investors wealth in 2021, given the start year, initial investment, and interest rate
def calculate_wealth_2021(name, year, initial_investment, interest_rate):
    current_wealth = initial_investment

    # loop through the years, adding the accrued interest each year
    while year < 2021:  # calculate until 2021
        current_wealth = current_wealth * (1 + interest_rate)  # calculate the new balance
        year += 1  # increment to the next year

    # print the final wealth in 2021 in a formatted sentence
    print("The year is " + str(year) + " A.D. and " + name + "'s bank account is at $" + str(current_wealth) + ".")

# test the function
calculate_wealth_2021("Brutus", start_year, BRUTUS_INITAL_INVESTMENT, BRUTUS_INTEREST_RATE)