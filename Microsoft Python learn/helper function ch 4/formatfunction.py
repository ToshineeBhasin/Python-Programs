medicine = 'Coughussin'
dosage = 5
duration = 4.5

#type 1
instructions = '{} - Take {} ML by mouth every {} hours'.format(medicine, dosage, duration)
print(instructions)
#Coughussin - Take 5 ML by mouth every 4.5 hours

#type 2
instructions = '{2} - Take {1} ML by mouth every {0} hours'.format(medicine, dosage,duration)
print(instructions)
#4.5 - Take 5 ML by mouth every Coughussin hours

#type 3
instructions = '{medicine} - Take {dosage} ML by mouth every {duration} hours '.format(medicine = 'Sneezergen', dosage = 10, duration = 6)
print(instructions)
#Sneezergen - Take 10 ML by mouth every 6 hours
