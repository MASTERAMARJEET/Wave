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

	def Wave_eq(self,r,E=1):
		self.E = E
		self.r = r
		Buffer = E*exp((np.dot(self.k,self.r) - self.omega*self.t)*1j)
		self.wave_eq = Buffer.real
		return self.wave_eq

	def help(self):
		print('This obect has following properties as of now:')
		print(f'wave_name:{self.wave_name}')
		print(f'wavelenght:{self.wavelenght}')
		print(f'frequency:{self.frequency}')
		print(f'E:{self.E}')
		print(f'k:{self.k}')
		print(f'r:{self.r}')
		print(f'wave_eq:{self.wave_eq}')
		
w1 = wave('apple',100)
R = np.array([10,9,8])
w1.Wave_eq(R)
print(w1.E)
w1.E = w1.E/sqrt(sum([p**2 for p in R]))
print(w1.E)
# f = 1
# Box = []
# for z in range(1):
# 	Box.append([])
# 	for y in range(1,50):
# 		Box[z-1].append([])
# 		for x in range(1):
# 			f = 1/sqrt(x**2 + y**2 + z**2)
# 			w1.r = np.array([x,y,z])
# 			S = w1.Wave_eq(np.array([10,10,10]), f)
# 			Box[z-1][y-1].append(S)
# print(Box)