#!/usr/bin/env 

import sys, getopt
from sass_parser import *
from doc_builder import *

def main(argv):
	inputfile = ''
	outputfile = 'sass_documentation.html'

	try:
		opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
	except getopt.GetoptError:
		print 'main.py -i <inputfile> -o <outputfile>'
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print 'main.py -i <inputfile> -o <outputfile>'
			sys.exit()
		elif opt in ("-i", "--ifile"):
			inputfile = arg
		elif opt in ("-o", "--ofile"):
			outputfile = arg

	Parser = Sass_Parser(inputfile)
	doc_raw = Parser.get_output()
	Doc_Builder(doc_raw, outputfile)

if __name__ == "__main__":
   main(sys.argv[1:])
