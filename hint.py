import sys
def List(dir):
	cmd = 'ls -l' + dir

def main ():
	List(sys.argv[1])
