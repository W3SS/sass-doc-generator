#!/usr/bin/env 

import os, fnmatch, re

class Sass_Parser:
	# Keep all sass filenames in a list
	sass_files = []

	# When a @doc tag is found get the class
	flag_doc_found = False
	flag_doc_long = False

	# List with the lines to be written in the output file
	output_content_raw = []

	# Two dimentional array for easier separation
	output_content_raw_2D = []

	def __init__(self, dir_path):
		self.dir_path = dir_path
		self.find_sass_files()
		self.read_files()

	# Create a list with the files to be parsed
	def find_sass_files(self):
		print "Parsing all files... "

		for root, dirnames, filenames in os.walk(self.dir_path):
			for filename in fnmatch.filter(filenames, '*.scss'):
				self.sass_files.append(os.path.join(root, filename))

		return self.sass_files

	# Read each line in the list line by line
	def read_files(self):
		for file_path in self.sass_files:
			with open(file_path) as file:
				for line in file:
					self.find_doc(line)
					self.find_class(line)

		return False

	def find_doc(self, line):
		if (-1 != line.find("@doc")):
			self.output_content_raw.append(line.strip(' \t\n'))
			self.flag_doc_found = True

		if (-1 != line.find("=> doc")):
			self.output_content_raw.append(line.strip(' \t\n'))
			self.flag_doc_found = True
			self.flag_doc_long = True
			return

		if (-1 == line.find("//")):
			self.flag_doc_long = False
			return
		
		if (True == self.flag_doc_long):
			line = line.split('// ', 1)[-1];
			self.output_content_raw.append(line.strip(' \t\n'))
			
	def find_class(self, line):
		if (False == self.flag_doc_found):
			return

		# Regex for finding classes
		regex_pattern = re.compile('^.*?\.-?[_a-zA-Z]+[_a-zA-Z0-9-]*\s*\{')
		
		if (regex_pattern.match(line)) :
			self.output_content_raw.append(line.strip(' \n\t'))
			self.flag_doc_found = False

			# Close the array element.
			self.output_content_raw_2D.append(self.output_content_raw)
			self.output_content_raw = []

		return False

	def get_output(self, two_dimentional_array = True):
		if(two_dimentional_array):
			return self.output_content_raw_2D
		return self.output_content_raw

	def print_output_content(self):
		print self.output_content_raw_2D
		return 1
