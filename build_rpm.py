import os
import sys
import shutil
import servbuild_setup as se

arch = "i386"

homedir = os.path.expanduser('~')
specfile = se.SOURCE_PACKAGE_PATH + "/rpmbuild/" + se.PACKAGE_NAME + ".spec"

try:
    if sys.argv[1] == "--arch":
	arch = sys.argv[2]
    else:
	print "Use python "+sys.argv[0]+" --arch arch"
	exit()
except:
    print "Use python "+sys.argv[0]+" --arch arch"
    exit()

build_path = os.getcwd() + "/" + se.SOURCE_PACKAGE_PATH + "/rpmbuild/" + se.PACKAGE_NAME+"-"+se.PACKAGE_VERSION+"_"+arch

def copyBinFiles():
    if not os.path.exists(build_path +"/usr"):
	os.makedirs(build_path +"/usr")
	
    if not os.path.exists(build_path +"/usr/bin/"):
	os.makedirs(build_path +"/usr/bin")
	
    lstFile = os.listdir(se.APPLICATION_PATH + "/bin")
    
    for file in lstFile:
	shutil.copyfile(se.APPLICATION_PATH + "/bin/" + file, build_path +"/usr/bin/" + file)

    
def copyLibFiles():
    if not os.path.exists(build_path +"/usr"):
	os.makedirs(build_path +"/usr")
	
    if not os.path.exists(build_path +"/usr/lib/"):
	os.makedirs(build_path +"/usr/lib/")
	
    lstFile = os.listdir(se.APPLICATION_PATH + "/lib")
    
    for file in lstFile:
	shutil.copyfile(se.APPLICATION_PATH + "/lib/" + file, build_path +"/usr/lib/" + file)


def copyIconFile():
    if not os.path.exists(build_path +"/opt"):
	os.makedirs(build_path +"/opt")
	
    if not os.path.exists(build_path +"/opt/" + se.APPLICATION_NAME):
	os.makedirs(build_path +"/opt/" + se.APPLICATION_NAME)

    shutil.copy(se.APPLICATION_ICON, build_path +"/opt/" + se.APPLICATION_NAME + "/")
    

def copyDesktopFile():
    if not os.path.exists(build_path +"/usr"):
	os.makedirs(build_path +"/usr")
	
    if not os.path.exists(build_path +"/usr/share/"):
	os.makedirs(build_path +"/usr/share/")

    if not os.path.exists(build_path +"/usr/share/applications/"):
	os.makedirs(build_path +"/usr/share/applications/")

    shutil.copy(se.APPLICATION_DESKTOP_FILE, build_path +"/usr/share/applications/")
       
    
if not os.path.exists(se.SOURCE_PACKAGE_PATH + "/rpmbuild/"):
    os.makedirs(se.SOURCE_PACKAGE_PATH+ "/rpmbuild/")
    
if not os.path.exists(se.SOURCE_PACKAGE_PATH + "/rpmbuild/tmpbuild"):
    os.makedirs(se.SOURCE_PACKAGE_PATH + "/rpmbuild/tmpbuild")
    
if not os.path.exists(build_path):
    os.makedirs(build_path)
    
#if not os.path.exists(build_path +"/"+ "DEBIAN"):
#    os.makedirs(build_path +"/"+ "DEBIAN")


################# BUILD OPEN SUSE RPM #####################

if os.path.exists(se.APPLICATION_PATH + "/bin"):
    copyBinFiles()

if os.path.exists(se.APPLICATION_PATH + "/lib"):
    copyLibFiles()
    
if se.APPLICATION_ICON <> "":
    copyIconFile()
    
if se.APPLICATION_DESKTOP_FILE <> "":
    copyDesktopFile()

    
file = open(se.SOURCE_PACKAGE_PATH + "/rpmbuild/" + se.PACKAGE_NAME + ".spec", 'w+')
file.write("Summary: "+se.PACKAGE_DESCRIPTION + "\n")
file.write("Name: "+se.PACKAGE_NAME + "\n")
file.write("Version: "+se.PACKAGE_VERSION + "\n")
file.write("Release: "+se.PACKAGE_VERSION + "\n")
file.write("License: "+se.PACKAGE_LICENSE + "\n")
file.write("Packager: "+se.PACKAGE_PACKAGER_NAME)
file.write("Group: "+se.PACKAGE_SECTION+"\n")
file.write("BuildRoot: "+ os.getcwd() + "/" + se.SOURCE_PACKAGE_PATH + "/rpmbuild/tmpbuild" + "\n")
file.write("Provides: "+se.PACKAGE_NAME + "\n")
file.write("Requires: "+se.PACKAGE_DEPENDS_RPM + "\n")
file.write("\n\n")

file.write("%description\n")
file.write(se.PACKAGE_DESCRIPTION + "\n\n")
file.write("%files\n")

for path, dirs, files in os.walk(build_path):
	p = path[len(build_path):]
	if dirs <> []:
		for dir in dirs:
			file.write("%dir " + str(p + "/" + dir + "/") + "\n")

	if files <> []:
		for file_name in files:
			file.write("\"" + str(p + "/" + file_name) + "\"\n")

file.close()

os.system("rpmbuild -bb --buildroot="+build_path+" "+specfile)


for path, dirs, files in os.walk(homedir + "/rpmbuild/RPMS/" + arch):
	if files <> []:
	      for file_name in files:
		      shutil.copy(path + "/" + file_name, se.SOURCE_PACKAGE_PATH + "/rpmbuild/" + se.PACKAGE_NAME + "-" + se.PACKAGE_SECTION + "_" + arch + "-" + "os.rpm")


################# BUILD Fedor RPM #####################

if os.path.exists(se.APPLICATION_PATH + "/bin"):
    copyBinFiles()

if os.path.exists(se.APPLICATION_PATH + "/lib"):
    copyLibFiles()
    
if se.APPLICATION_ICON <> "":
    copyIconFile()
    
if se.APPLICATION_DESKTOP_FILE <> "":
    copyDesktopFile()

file = open(se.SOURCE_PACKAGE_PATH + "/rpmbuild/" + se.PACKAGE_NAME + ".spec", 'w+')
file.write("Summary: "+se.PACKAGE_DESCRIPTION + "\n")
file.write("Name: "+se.PACKAGE_NAME + "\n")
file.write("Version: "+se.PACKAGE_VERSION + "\n")
file.write("Release: "+se.PACKAGE_VERSION + "\n")
file.write("License: "+se.PACKAGE_LICENSE + "\n")
file.write("Packager: "+se.PACKAGE_PACKAGER_NAME)
file.write("Group: "+se.PACKAGE_SECTION+"\n")
file.write("BuildRoot: "+ os.getcwd() + "/" + se.SOURCE_PACKAGE_PATH + "/rpmbuild/tmpbuild" + "\n")
file.write("Provides: "+se.PACKAGE_NAME + "\n")
file.write("Requires: "+se.PACKAGE_DEPENDS_RPM_FEDORA + "\n")
file.write("\n\n")

file.write("%description\n")
file.write(se.PACKAGE_DESCRIPTION + "\n\n")
file.write("%files\n")     

for path, dirs, files in os.walk(build_path):
	p = path[len(build_path):]
	if dirs <> []:
		for dir in dirs:
			file.write("%dir " + str(p + "/" + dir + "/") + "\n")

	if files <> []:
		for file_name in files:
			file.write("\"" + str(p + "/" + file_name) + "\"\n")

file.close()

os.system("rpmbuild -bb --buildroot="+build_path+" "+specfile)

for path, dirs, files in os.walk(homedir + "/rpmbuild/RPMS/" + arch):
	if files <> []:
	      for file_name in files:
		      shutil.copy(path + "/" + file_name, se.SOURCE_PACKAGE_PATH + "/rpmbuild/" + se.PACKAGE_NAME + "-" + se.PACKAGE_SECTION + "_" + arch + "-" + "fr.rpm")