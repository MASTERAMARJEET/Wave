from math import pi, sqrt
from cmath import exp
import numpy as np
import matplotlib.pyplot as plt

class wave():
	c = 3*(10**8)					#unit-> m/sec
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

	def Wave_eq(self,r,A=1):
		self.A = A
		self.r = r
		Buffer = A*exp((np.dot(self.k,self.r) - self.omega*self.t)*1j)
		self.wave_eq = Buffer.real
		return self.wave_eq

	def help(self):
		print('This obect has following properties as of now:')
		print(f'wave_name:{self.wave_name}')
		print(f'wavelenght:{self.wavelenght}')
		print(f'frequency:{self.frequency}')
		print(f'A:{self.A}')
		print(f'k:{self.k}')
		print(f'r:{self.r}')
		print(f'wave_eq:{self.wave_eq}')
