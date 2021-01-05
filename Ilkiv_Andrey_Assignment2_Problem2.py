#Andrey Ilkiv Assignent 2 9/30/2020 Section 01 problem 2

#Asks user to enter value 1 and stores it as an interger
Num1 = int(input('Enter value 1: '))

#Asks user to enter value 2 and stores it as an interger
Num2 = int(input('Enter value 2: '))

#prints heading for place value totals and prints empty line
print('' , 'Place Value Totals:', '' , sep='\n')

#Gets the number in the thousands place from user input value 1
x0 = Num1 // 1000

#Gets the number in the hundreds place from user input value 1
x1 = (Num1 - x0*1000) // 100

#Gets the number in the tens place from user input value 1
x2 = (Num1 - x0*1000 - x1*100) // 10

#Gets the number in the ones place from user input value 1
x3 = Num1 - x0*1000 - x1*100 - x2*10

#Gets the number in the thousands place from user input value 2
y0 = Num2 // 1000

#Gets the number in the hundreds place from user input value 2
y1 = (Num2 - y0*1000) // 100

#Gets the number in the tens place from user input value 2
y2 = (Num2 - y0*1000 - y1*100) // 10

#Gets the number in the ones place from user input value 2
y3 = Num2 - y0*1000 - y1*100 - y2*10

#sums the values in the ones place up
ones = x3 + y3

#sums the values in the tens place up
tens = x2 + y2

#sums the values in the hundreds place up
hundreds = x1 + y1

#sums the values in the thousands place up
thousands = x0 + y0

#prints the sum of the ones spaces
print('       ' + str(x3) + ' + ' + str(y3) + ' = ' + str(ones) + ' one(s)')

#prints the sum of the tens spaces
print('       ' + str(x2) + ' + ' + str(y2) + ' = ' + str(tens) + ' ten(s)')

#prints the sum of the hundreds spaces
print('       ' + str(x1) + ' + ' + str(y1) + ' = ' + str(hundreds) + ' hundred(s)')

#prints the sum of the thousands spaces
print('       ' + str(x0) + ' + ' + str(y0) + ' = ' + str(thousands) + ' thousand(s)')
