import random
import string
import os
import getpass
os.system('start https://github.com/velx007')
length = random.randint(12,25)
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation
all = lower + upper + num + symbols
temp = random.sample(all,length)
password = "".join(temp)
print('Password', password)
os.system('pause')
