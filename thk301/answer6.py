#Tae Kim
#HW 4-6

first_name = raw_input ('Enter your first name: ')
last_name= raw_input('Enter your last name: ')
print 'Enter your date of birth: '
month= raw_input('Month? ')
try:
     day= int(input('Day? '))
except:
     print "It was not a number. Please type in the day in number"
     day= int(input('Day? '))
try:
    year= int(input('Year? '))
except:
    print "It was not a number. Please type in the year in number"
    year= int(input('Year? '))    

print first_name, last_name, "was born on", month,str(day)+", "+str(year)+"."

