#Assigning variables

meal = 44.50
tax = 6.75/100
tip = 0.15

tax_value = tax * meal
meal_with_tax = meal + tax_value
tip_value = meal_with_tax * tip

total = meal_with_tax + tip_value

print "The base cost of your meal was $%.2f" % (meal)
print "You need to pay $%.2f" % (tax_value)
print "Tipping at a rate of %d%%, you should leave $%.2f for a tip." % (tip * 100, tip_value)
print "The grand total of your meal is $%.2f" % (total)