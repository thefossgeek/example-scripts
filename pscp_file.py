#!/usr/bin/python
import pexpect
import time
import sys
import getopt
def usage():
	print 'pscp_file.py -u <username> -p <password> -i <remote ip address>'
	sys.exit(1)

def main(argv):
	src_file='/opt/pcube/sm/server/bin/subscribers.csv'
	dst_path='/var/tmp'
	try:
		opts, args = getopt.getopt(argv, "hu:p:i:", ["help", "username=", "password=",'ipaddress='])
	except getopt.GetoptError:          
		usage()                         
		sys.exit(1)    
	for opt, arg in opts:
		if opt in ("-h", "--help"):
			usage()
		elif opt in ("-u", "--username"):
			user = arg
		elif opt in ("-p", "--password"):
			password = arg
		elif opt in ("-i", "--ipaddress"):
			host = arg
	print 'scp %s %s@%s:%s' % (src_file, user, host, dst_path)
	child = pexpect.spawn('scp %s %s@%s:%s' % (src_file, user, host, dst_path))
	i = child.expect(['assword:', r"yes/no"], timeout=20)
	if i == 0:
		child.sendline(password)
		child.expect(pexpect.EOF)
	elif i == 1:
		child.sendline("yes")
		child.expect("assword:", timeout=30)
		child.sendline(password)
		child.expect(pexpect.EOF)

if __name__ == "__main__":
	main(sys.argv[1:])
