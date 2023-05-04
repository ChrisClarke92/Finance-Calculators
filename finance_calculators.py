import math

investmentSelected = False   #Booleans that change to 'True' once the user has input the relevant responses
bondSelected = False
inputCorrect = False

print('Investment - To calculate the amount of interest you will earn on your investment.')
print('Bond - To calculate the amount you will have to pay on a home loan.')
print("")
    
while inputCorrect == False:   #Asks the user to input until they correctly type Investment or Bond
    choice = input('Enter either Investment or Bond from the list above: ').lower()   # .lower() ensures the input will not be affected by caps
    
    if choice == 'investment':   #If and Elif statements let the code know what to do once the user has input
        investmentSelected = True
        inputCorrect = True      #The while loop breaks if True
    elif choice == 'bond':
        bondSelected = True
        inputCorrect = True
    else:
        print('Invalid entry. Please make sure you enter either Investment or Bond.')  #inputCorrect remains false and while loop continues to run
    
if investmentSelected == True:   #Once the while loop is complete, this If statement begins. This section is the Investment calculator
    deposit = int(input('The money I am depositing in pounds is: '))  #int() is used to convert the input to an integer for calculations
    rate = float(input('My interest rate as a percentage is: '))  #float() is used in the same way as int() but for decimal numbers
    years = int(input('The number of years I plan to invest is: '))
    interest = input('Would you like simple or compound interest? ').lower()
    
    simple = False
    compound = False
    
    newRate = rate/100  #divides the rate by 100 for the percentage part of the formula
    
    if interest == 'simple':
        simple = True
        if simple == True:
            A = deposit*(1 + newRate*years)  #simple interest formula based on the user inputs
            print("")
            print('Your investment return will be: £' + str(A))  #converted 'A' into a String so that I can concatenate with other text
    elif interest == 'compound':
        compound = True
        if compound == True:
            A = deposit * math.pow((1+newRate),years)  #compound interest formula based on the user inputs
            print("")
            print('Your investment return will be: £' + str(A))

elif bondSelected == True:  #This section is the Bond calculator
    value = int(input('The value of my house in pounds is: '))
    rate = float(input('My interest rate is: '))
    months = int(input('Months I will take to repay my bond: '))
    
    newRate = rate/100   #divided by 100 for the percentage calculation
    newerRate = newRate/12   #divided by 12 for the months in the year
    
    repayment = (newerRate * value)/(1 - (1 + newerRate)**(-months))  #bond repayment formula based on user inputs
    print("")
    print('Your monthly repayments will be: £' + str(repayment))  
