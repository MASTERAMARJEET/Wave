from math import pi, sqrt, cos
import numpy as np

class em_wave():
	
	c = 3*(10**8)					#unit-> m/sec
	E = np.array([1, 0])
	phi = np.array([0, 0])
	vector = np.array([1,0])
	k_unit = np.array([0,0,1])		#unit-> 1/m
	r = np.array([0,0,1])			#unit-> 1/m
	t = 0							#unit-> sec
	
	def __init__(self,name,wavelenght):
		self.wave_name = name
		self.wavelenght = wavelenght
		self.frequency = self.c/self.wavelenght
		self.k = (2*pi/self.wavelenght)*self.k_unit
		self.omega = 2*pi/self.frequency
	
	def __repr__(self):
		return 'This is a wave object which can given all the proprties that a wave should have.For more info. type object.help()'

	def set_eq(self,E,phi):
		self.E = np.array(E)
		self.phi = np.array(phi)
		self.wave_eq = np.array([P*cos(np.dot(self.k,self.r) - self.omega*self.t + Q) for P,Q in zip(self.E,self.phi)])

	def Wave_eq(self,r):
		self.r = r
		self.wave_eq = np.array([P*cos(np.dot(self.k,self.r) - self.omega*self.t + Q) for P,Q in zip(self.E,self.phi)])
		return self.wave_eq

	def help(self):
		print('This obect has following properties as of now:')
		print(f'wave_name:{self.wave_name}')
		print(f'wavelenght:{self.wavelenght}')
		print(f'frequency:{self.frequency}')
		print(f'E:{self.E}')
		print(f'k:{self.k}')
		print(f'r:{self.r}')
		print(f'phi:{self.phi}')
		print(f'wave_eq:{self.wave_eq}')
