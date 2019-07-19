from math import pi,sqrt
from cmath import exp
import numpy as np
import matplotlib.pyplot as plt

class wave():
	c = 3*(10**8)
	A = 1
	k_unit = np.array([0,0,1])
	r = np.array([0,0,1])
	t = 0
	def __init__(self,name,wavelenght):
		self.wave_name = name
		self.wavelenght = wavelenght
		self.frequency = self.c/self.wavelenght
		self.k = (2*pi/self.wavelenght)*self.k_unit
		self.omega = 2*pi/self.frequency
	
	def __repr__(self):
		return 'This is a wave object which can given all the proprties that a wave should have.For more info. type object.help()'

	def Wave_eq(self,A,k_unit):
		k_unit = k_unit/sqrt(sum([p**2 for p in k_unit]))
		self.A = A
		self.k_unit = k_unit
		Buffer = A*exp((np.dot(self.k,self.r) - self.omega*self.t)*1j)
		self.wave_eq = Buffer.real
		return self.wave_eq

	def help(self):
		print('This obect has following properties as of now:')
		print('wave_name:{}'.format(self.wave_name))
		print('wavelenght:{}'.format(self.wavelenght))
		print('frequency:{}'.format(self.frequency))
		print('A:{}'.format(self.A))
		print('k:{}'.format(self.k))
		print('r:{}'.format(self.r))
		print('wave_eq:{}'.format(self.wave_eq))
		
w1 = wave('apple',100)

f = 1
Box = []
for z in range(1,5):
	Box.append([])
	for y in range(1,5):
		Box[z-1].append([])
		for x in range(1,5):
			# f = 1/sqrt(x**2 + y**2 + z**2)
			w1.r = np.array([x,y,z])
			S = w1.Wave_eq(f, np.array([10,10,10]))
			Box[z-1][y-1].append(S)
print(Box)