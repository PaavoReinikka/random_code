#!/usr/bin/env python3

from codetools.codegrep import codegrep


if __name__ == "__main__":
	"""
	$ python codecat.py file.py pattern <language>

	"""
	import sys
	file_path = sys.argv[1]
	pattern = sys.argv[2]
	language = sys.argv[3] if len(sys.argv) > 3 else "python"
	codegrep(file_path, pattern, language)

