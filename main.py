#!/usr/bin/env 

from sass_parser import *
from doc_builder import *

Parser = Sass_Parser("../menu/assets")
doc_raw = Parser.get_output()

Doc_Builder = Doc_Builder(doc_raw)
