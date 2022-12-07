miles_per_gallon = float(input())
dollars_per_gallon = float(input())
unit_cost = dollars_per_gallon / miles_per_gallon
your_value1 = unit_cost * 20
your_value2 = unit_cost * 75
your_value3 = unit_cost * 500
print('{:.2f} {:.2f} {:.2f}'.format(your_value1, your_value2, your_value3))