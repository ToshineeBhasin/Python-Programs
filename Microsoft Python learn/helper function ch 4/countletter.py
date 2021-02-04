location = 'Mississippi'
print(location.count('s'))      #4

print(len('Toshinee Bhasin'))   #15

msg = 'racecar'
print(msg.startswith('r'))
print(msg.startswith('a'))
print(msg.startswith('ra'))

print(msg.endswith('r'))
print(msg.endswith('a'))
print(msg.endswith('ar'))
'''
True
False
True
True
False
True
'''

msg = 'The quick brown fox jumps over the lazy dog'
print(msg.find('q'))            #4
print(msg.find('t'))            #31
print(msg.find('T'))            #0


msg = '     middle   '
print('.'+ msg.lstrip() +'.')
print('.'+ msg.rstrip() +'.')
print('.'+ msg.strip() +'.')
'''
.middle   .
.     middle.
.middle.
'''

msg = 'brevity is the essence of wit'
msg = msg.replace('essence','soul')
print(msg)          #brevity is the soul of wit


