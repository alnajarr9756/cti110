# CTI-110
# P4HW2 - Salary Calculator
# Rana Alnajar
# 12-2-2022
#
#The program below gets input from user about pay rate and hours worked that would need to be calcuates.
#It calcuates overtime , regular hours, and gross pay.
#Enter employee name.
#Enter hourly pay.
#The program calculates employee's regular hours and gross pay based on hours work and hourly rate.
#It gives the total amount payed for overtime, regular hours, and gross pay based on the calculates above.
#
count, payOverTime, payRegHr, payGross = 0,0,0,0 

name = input("Enter employee's name or 'None' to terminate: ") 
while (name != 'None') and (name != None) and (name != 'none'): 
    count += 1
    workHr = float(input("How many hours did " + name + " worked? "))
    rate = float(input("What is " + name + "\'s pay rate? "))
    overTm = 0
    
    if workHr > 40:
        overTm = workHr - 40 
    
    overTmPay = overTm * rate * 1.5 
    RegHrPay = workHr * rate
    grossPay = overTmPay + RegHrPay
    
    print(f"\nEmployee name: {name}", end='\n\n')
     
    print ("{:<15} {:<11} {:11} {:<15} {:<14} {:<12}".format('Hours Worked', 'Pay Rate', 'OverTime', 'OverTime Pay', 'RegHour Pay', 'Gross Pay'))
    
    line = 85 * '-'
    print(line)
    
    payOverTime += overTmPay
    
    payRegHr += RegHrPay
     
    payGross += grossPay
    
    print ("{:<15} {:<11} {:<11} {:<15} ${:<14,.2f} ${:<12,.2f}".format(workHr, rate, overTm, overTmPay, RegHrPay, grossPay), end = "\n\n\n") 
    name = input("Enter employee's name or 'None' to terminate: ") 

print()
print (f" Total number of employees entered: {count}")
print (f" Total amount payed for overtime: ${payOverTime:.2f}") 
print (f" Total amount payed for regular hours: ${payRegHr:.2f}")
print (f" Total amount payed in gross: ${payGross:.2f}")