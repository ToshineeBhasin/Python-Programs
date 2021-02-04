temp = input("What is the temperature in Fahrenheit ? ")

if temp.isnumeric() == False:
    print("Input is not a number")
    exit()
else:
    cel = ((int(temp) - 32)* 5/9)
    print("Temperature in celcius is ",str(cel))

'''
What is the temperature in Fahrenheit ? tosh
Input is not a number
or
What is the temperature in Fahrenheit ? 55
Temperature in celcius is  12.777777777777779
'''