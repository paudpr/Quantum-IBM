class CsvReader(object):
	def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
		self.filename = open(filename, 'r')
		self.content = []
		self.sep = sep
		for line in self.filename.read().split('\n'):
			line.split(self.sep)
			self.content.append(line)
		self.header = header
		self.skip_top = skip_top
		self.skip_bottom = skip_bottom

	def __enter__(self):
		return self

	def __exit__(self, exc_type, exc_value, traceback):
		return self.filename.close()

	def getdata(self):
		len = 0
		for line in self.content:
			len += 1
		i = self.skip_top
		aux_content = []
		for i in range(i, len - self.skip_bottom):
			aux_content.append(self.content[i].split(','))
		return aux_content

	def getheader(self):
		if self.header == False:
			return self.content[0].split(',')
		else:
			return 'No header in file'



# if __name__ == "__main__":
# 	with CsvReader('good.csv') as file:
# 		data = file.getdata()
# 		print(data)
# 		print(len(data))
# 		header = file.getheader()
# 		print(header)
# 		print(len(header))
