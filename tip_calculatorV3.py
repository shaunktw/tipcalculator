import sys
from optparse import OptionParser

#Assigning variables
parser = OptionParser()
parser.add_option("-m", "--meal", dest = "meal", type = "float", help = "the base cost of the meal")
parser.add_option("-x", "--tax", dest = "tax", type= "float",  help = "the raw tax value")
parser.add_option("-t", "--tip", dest = "tip", type = "float", help = "the tip that is required", default = 0.20)

(options, args) = parser.parse_args()
if not (options.meal and options.tax):
	parser.error("You need to supply the meal price and the tax")

tax_value = (options.tax/100) * options.meal
meal_with_tax = options.meal + tax_value
tip_value = meal_with_tax * (options.tip/100)

total = meal_with_tax + tip_value


print "The base cost of your meal was ${0:.2f}".format(options.meal)
print "You need to pay ${0:.2f} for tax".format(tax_value)
print "Tipping at a rate of {0:.2f}%, you should leave ${1:.2f} for a tip.".format(options.tip, tip_value)
print "The grand total of your meal is ${0:.2f}".format(total)