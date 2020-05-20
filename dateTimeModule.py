'''
Created on 20-May-2020

@author: Toshinee Bhasin
'''
import datetime
x = datetime.datetime.now()
print(x)

'''
output:
2020-05-20 17:09:26.610724
'''

import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))
'''
output:
2020
Wednesday
'''