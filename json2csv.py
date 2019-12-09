import json
import sys

class json2csv:
	'''Convert json file to csv file. Input to the program is a json file and and output file name to hold csv'''
	def __init__(self,jfile, cfile):
		self.jfile=jfile
		self.cfile=cfile

	def convert2csv(self):
		''' Function that performs conversion operation'''
		try:
			with open(self.jfile) as jf:
				data=json.load(jf)
			
			with open(self.cfile, "w+") as cf:
				cf.write(','.join(dict(data[0]).keys()) + "\n")
		
			with open(self.cfile, "a+") as cf:
				for val in data:
					cf.write(','.join(dict(val).values()) + "\n")

		except Exception as e:
			print("JSON file error => %s" % str(e))

if(__name__ == "__main__"):
	if(len(sys.argv) == 2):
		jfile=sys.argv[1]
		cfile=sys.argv[2]
	else:
		print("Invalid number of arguments")
		print("Usage: json2csv <json file> <csv file>")
		sys.exit()

	c2s=json2csv(jfile,cfile)
	c2s.convert2csv()
