# Define a function that takes a principal mortgage amount, an interest rate, and an amortization period; intention of function is to calculate and return mortgage payments
def mortgage_payments(principal, rate, amortization):

# Calculate the interest rates that will be used in the payment calculations; the rate will be different depending on the type of payment
    rate_monthly = (1 + rate/100/2)**(2/12) - 1
    rate_semi_monthly = (1 + rate/100/2)**(2/24) - 1
    rate_bi_weekly = (1 + rate/100/2)**(2/26) - 1
    rate_weekly = (1 + rate/100/2)**(2/52) - 1

# Calculate the number of payment periods there will be in a year depending on the type of payment
    periods_monthly = amortization * 12
    periods_semi_monthly = amortization * 24
    periods_bi_weekly = amortization * 26
    periods_weekly = amortization * 52

# Calculate the payment using the present value of an annuity formula
    monthly_payment = principal * (rate_monthly / (1 - (1 + rate_monthly)**-periods_monthly))
    semi_monthly_payment = principal * (rate_semi_monthly / (1 - (1 + rate_semi_monthly)**-periods_semi_monthly))
    bi_weekly_payment = principal * (rate_bi_weekly / (1 - (1 + rate_bi_weekly)**-periods_bi_weekly))
    weekly_payment = principal * (rate_weekly / (1 - (1 + rate_weekly)**-periods_weekly))
    rapid_bi_weekly_payment = monthly_payment / 2
    rapid_weekly_payment = rapid_bi_weekly_payment / 2

# Return the values as a tuple
    return (monthly_payment, semi_monthly_payment, bi_weekly_payment, weekly_payment, rapid_bi_weekly_payment, rapid_weekly_payment)

# Get users' input for the interest rate, amortization, and principal
rate = float(input("Please enter the stated interest rate on your mortgage (as a %): "))
amortization = int(input("Please enter the amortization period on your mortgage (in years): "))
principal = int(input("Please enter the principal amount of your mortgage (in $): "))

# Give the tuple with stored calculations a variable name, so that the payments can be indexed for printing
periodic_payments = mortgage_payments(principal, rate, amortization)

# Statements to print the output of each index in the tuple; :.2f is used to ensure 2 decimal places always show up, round function omits 0s in the hundreths place
print("Below are your payment options:"
      "\nMonthly Payment: ${:.2f}".format(periodic_payments[0]),
      "\nSemi-Monthly Payment: ${:.2f}".format(periodic_payments[1]),
      "\nBi-Weekly Payment: ${:.2f}".format(periodic_payments[2]),
      "\nWeekly Payment: ${:.2f}".format(periodic_payments[3]),
      "\nRapid Bi-Weekly Payment: ${:.2f}".format(periodic_payments[4]),
      "\nRapid Weekly Payment: ${:.2f}".format(periodic_payments[5]))