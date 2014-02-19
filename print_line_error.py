import sys
import re

def main(argv):
	in_file = get_file_from_argv(argv)
	for line in in_file:
		outline = process_single_line(line)
	in_file.close()


def process_single_line(line):
	if "error" in line:
		print line
	if "warn" in line:
		print line
	if "ERROR" in line:
		print line
	if "WARN" in line:
		print line

def get_file_from_argv(argv):
	filename = argv[1]
	f = open(filename)
	return f


def print_usage():
    print """
    Usage: Print ERROR from file.
    """
    
if __name__ == '__main__':
    if len(sys.argv) < 1:
        print_usage()
    else:
        main(sys.argv)
