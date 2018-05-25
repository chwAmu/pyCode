# Directly import
import module1
module1.say_hello()
print(module1.var_mod1)

# import and shortly the name by using keyword as
import module1 as m1
m1.say_hello()
print(m1.var_mod1)

# import some function only
from module1 import say_hello,var_mod1
say_hello()
print(var_mod1)

# 
from module1 import say_hello as ho1
ho1()

# change the syspath
# '/Users/username/Documents/GitHub/python/modules'
# import the modules inside same directory first
import sys
# print(sys.path)
# sys.path.append('the location that you want to append')
# nano -/.bash_profie
# go to the end the files.
# export PYTHONPATH="your location"
# ctrl+x to save
# you can import your modules without the append function.

# import the standard modules
import random
import datetime
import calendar

li=['a22',1,4,5,'44a','c1']
rn=random.choice(li)
print(rn)

today=datetime.date.today()
print(today)

print(calendar.isleap(2017))

# enable to access the unline modules
# print the working directory
import os

print(os.getcwd())
print(os.__file__)




