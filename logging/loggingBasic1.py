import logging
"""
logging level allow us to specify exactly what we want to log
by separating these into categories. and we have 5 standard
level.
-debug 10
-info	20
-warning 30
-error	40
-critcal	50
default level of the logging is set to warning.
"""

# make sure is logging.DEBUG is in cap letters.
# it is just a constant
# https://docs.python.org/3/library/logging.html#logrecord-attributes
# to find which format that you would like to use
logging.basicConfig(filename='testing.log',level=logging.DEBUG,
	format='%(asctime)s,%(levelname)s,%(message)s')

def add(x,y):
	return x+y

def sub(x,y):
	return x-y

def mult(x,y):
	return x*y

def div(x,y):
	return x/y


x=4
y=5

a=add(x,y)
logging.debug('add : {} + {} = {} '.format(x,y,a))
