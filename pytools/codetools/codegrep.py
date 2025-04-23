from rich.console import Console
from rich.syntax import Syntax
import re
from codetools.codecat import _codecat

def codegrep(file_path: str, pattern: str, language: str = "python") -> None:
	"""
	Searches a function name (pattern) in a file and prints the function code.
	The function maps starting point with 'def <pattern>', and endpoing with the next 'def' or EOF.
	"""
	with open(file_path, "r") as file:
		code = file.read()
		lines = code.split("\n")
		start = None
		for i, line in enumerate(lines):
			if re.search(f"^def {pattern}", line):
				start = i
				break
		if start is not None:
			for i in range(start, len(lines)):
				#if lines[i].startswith("def") and i != start:
				
				if re.search(r"^[def]|^[class]|^[@]|^[if]", lines[i]) and i != start:
					end = i
					break
			else:
				end = len(lines)
			_codecat("\n".join(lines[start:end]), language)
		else:
			print(f"pattern '{pattern}' not found in {file_path}.")

