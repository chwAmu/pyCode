import logging

logging.basicConfig(filename='motor.log',level=logging.INFO,format='%(levelname)s,%(message)s')

class Motor:

	def __init__(self,voltage,current):
		self.voltage=voltage
		self.current=current
		logging.info('Motor profile is created with :{}V and {}A'.format(self.voltage,self.current))

	@property
	def getPower(self):
		return '{} * {} = {}'.format(self.current,self.voltage,self.current*self.voltage)

	@property
	def getDat(self):
		return 'v={},a={}'.format(self.voltage,self.current)



m1=Motor(380,2)
m2=Motor(220,1.4)
	
	