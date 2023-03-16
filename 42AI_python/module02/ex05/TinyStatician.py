import math
import copy

class TinyStatistician:
	def __init__(self):
		pass

	@staticmethod
	def mean(self):
		if not hasattr(self, '__iter__'):
			print('ERROR: This method only works with iterables')
		if len(self) == 0:
			return None
		total = 0
		for item in self:
			if not isinstance(item, int) and not isinstance(item, float):
				return 'ERROR: All items in iterable input must be numeric'
			total += item
		return (float(total / len(self)))

	@staticmethod
	def median(self):
		if not hasattr(self, '__iter__'):
			print('ERROR: This method only works with iterables')
		if len(self) == 0:
			return None
		self.sort()
		if len(self) % 2 == 0:
			med = self[(len(self)/2) - 1] + self[len(self) / 2]
			return float(med / 2)
		else:
			return float(self[int((len(self)/2) - 0.5)])

	@staticmethod
	def quartiles(self):
		if not hasattr(self, '__iter__'):
			print('ERROR: This method only works with iterables')
		if len(self) == 0:
			return None
		self.sort()
		in_q1 = 0.25 * len(self) + 1
		if in_q1 - math.floor(in_q1) == 0:
			q1 = self[in_q1]
		else: 
			q1 = self[math.floor(in_q1)] + (math.ceil(in_q1) - math.floor(in_q1)) * (self[math.floor(in_q1) - 1] - self[math.ceil(in_q1) - 1])
		in_q3 = 0.75 * len(self) + 1
		if in_q3 - math.floor(in_q3) == 0:
			q3 = self[in_q3]
		else:
			q3 = self[math.floor(in_q3)] + (math.ceil(in_q3) - math.floor(in_q3)) * (self[math.floor(in_q3) - 1] - self[math.ceil(in_q3) - 1])
		return list((float(q1), float(q3)))

	@staticmethod
	def var(self):
		if not hasattr(self, '__iter__'):
			print('ERROR: This method only works with iterables')
		if len(self) == 0:
			return None
		vari = 0
		mean = TinyStatistician.mean(self)
		for item in self:
			vari += (item - mean)**2
		return float(vari/len(self))

	@staticmethod
	def std(self):
		if not hasattr(self, '__iter__'):
			print('ERROR: This method only works with iterables')
		if len(self) == 0:
			return None
		std = math.sqrt(TinyStatistician.var(self))
		return float(std)






# tstat = TinyStatistician()
# a = [1, 42, 300, 10, 59]
# print(tstat.mean(a))
# print(tstat.median(a))
# print(tstat.quartiles(a))
# print(tstat.var(a))
# print(tstat.std(a))


