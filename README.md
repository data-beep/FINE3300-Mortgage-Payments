 # FINE3300-Mortgage-Payments
This python program calculates monthly, semi-monthly, bi-weekly, weekly, rapid bi-weekly and rapid weekly mortgage payments.

## Features

- **Process Basic User Input**

  - Gets user to input their:
  	- Mortgage amortization rate
  	- Quoted interest rate
  	- Mortgage principal
   
- **Performs Present Value Calculations**
 	 
  - Calculates present value of the mortgage and then calculates periodic payments
  - This is done using the present value of an annuity formula given by:
 	- P * (r / (1 - (1 + r)^-n)) where P is the principal amount, r is the stated interest rate, and n is the number of periods

## Conclusion
- The payments are calculated and returned as a tuple using the function, mortgage_payment, and then formatting is done in the print statements

