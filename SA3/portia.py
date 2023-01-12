# filename: portia.py
# author:   Valerie Gadapati
# date:     Jan 11, 2023
# purpose:  compare the wealth of two ancient romans to see when one surpasses the other

# define variables about Brutus and Portia's investments
BRUTUS_INITIAL_INVESTMENT = 1.00
BRUTUS_INTEREST_RATE = 0.05
PORTIA_INITIAL_INVESTMENT = 100000
PORTIA_INTEREST_RATE = 0.04
year = 0  # the start year

brutus_wealth = BRUTUS_INITIAL_INVESTMENT
portia_wealth = PORTIA_INITIAL_INVESTMENT

# continue calculating their total wealth until Brutus surpasses Portia
while brutus_wealth < portia_wealth: # continue calculating their total wealth until Brutus surpasses Portia
    brutus_wealth = brutus_wealth * (1 + BRUTUS_INTEREST_RATE)
    portia_wealth = portia_wealth * (1 + PORTIA_INTEREST_RATE)
    year += 1  # increment to the next year

# print the year and wealths when the surpass occurs
print("The year is " + str(year) + " A.D. and Brutus's bank account is at $" + str(brutus_wealth) + ", and Portia's is at $" + str(portia_wealth))