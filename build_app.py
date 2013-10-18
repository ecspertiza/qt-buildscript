import os
import sys
import servbuild_setup as se

arch = "i386"

try:
    if sys.argv[1] == "--arch":
	arch = sys.argv[2]
    else:
	print "Use python "+sys.argv[0]+" --arch arch"
	exit()
except:
    print "Use python "+sys.argv[0]+" --arch arch"
    exit()

os.system(se.QMAKE_NAME + " " + se.APPLICATION_PRO)
os.system("make -f "+se.APPLICATION_MAKEFILE)