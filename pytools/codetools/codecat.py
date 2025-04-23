from rich.console import Console
from rich.syntax import Syntax
import re


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
			print(f"Function {pattern} not found in {file_path}.")


def _codecat(text: str, language: str = "python") -> None:
	syntax = Syntax(text, language, theme="monokai", line_numbers=True)
	console = Console()
	print()
	console.print(syntax)
	print()

def codecat(file_path: str, language: str = "python") -> None:
	with open(file_path, "r") as file:
		code = file.read()
		_codecat(code, language)

if __name__ == "__main__":
	"""
	$ python codecat.py file.py <language>

	"""
	import sys
	file_path = sys.argv[1]
#	pattern = sys.argv[2]
#	language = sys.argv[3] if len(sys.argv) > 3 else "python"
	language = sys.argv[2] if len(sys.argv) > 2 else "python"
	codecat(file_path, language)
	#codegrep(file_path, pattern, language)





