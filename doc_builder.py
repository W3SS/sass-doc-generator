#!/usr/bin/env 

import os

class Doc_Builder:
	input_content_raw = []
	output_content = []
	output_file = ''

	def __init__(self, input_content_raw = [], file_name = 'sass_documentation.html'):
		self.input_content_raw = input_content_raw
		self.output_file = file_name
		self.build_html()

	def build_html(self):
		file = open(self.output_file, 'w')

		# The data thats gathered fromt he Sass_Parser class
		html_content = self.generate_content()
		
		# The base HTML structure
		html_structure = """<html>
			<head>
				<link rel='stylesheet' href='style.css' />
				<title>Sass Documenter v1.0</title>
			</head>
			<body>
				<div class='documentation-wrapper'>
				%(html_content)s
				</div>
			</body>
		</html>
		"""%{'html_content':html_content}
		
		# Get it all in the file and we are done :)
		file.write(html_structure)
		file.close()

	def generate_content(self):
		content = ''

		for wrapper in self.input_content_raw:
			# Each @doc and class pair
			content += "<div class='doc-content'>"
			content += "<h2>" + wrapper[-1].strip("{}") + "</h2>"
			for item in wrapper[:-1]:
				content += item.strip("// @doc =>")
			content += "</div>"

		return content
