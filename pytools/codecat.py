#!/usr/bin/env python3

from codetools.codecat import codecat

if __name__ == "__main__":
	"""
	$ python codecat.py file.py <language>

	"""
	import sys
	file_path = sys.argv[1]
	language = sys.argv[2] if len(sys.argv) > 2 else "python"
	codecat(file_path, language)

