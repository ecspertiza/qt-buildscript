import os
import sys
import shutil
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

build_path = se.SOURCE_PACKAGE_PATH + "/debbuild/" + se.PACKAGE_NAME+"-"+se.PACKAGE_VERSION+"_"+arch

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
       
    
if not os.path.exists(se.SOURCE_PACKAGE_PATH + "/debbuild/"):
    os.makedirs(se.SOURCE_PACKAGE_PATH+ "/debbuild/")
    
for distr in se.PACKAGE_DISTR_DEPENDS:
      
      if distr["type"] == "deb":
	    build_path = se.SOURCE_PACKAGE_PATH + "/debbuild/" + se.PACKAGE_NAME+"-"+se.PACKAGE_VERSION+"_"+arch + "-" + distr["name"] + str(distr["ver"])
	
	    if not os.path.exists(build_path):
		os.makedirs(build_path)
		
	    if not os.path.exists(build_path +"/"+ "DEBIAN"):
		os.makedirs(build_path +"/"+ "DEBIAN")

	    if os.path.exists(se.APPLICATION_PATH + "/bin"):
		copyBinFiles()

	    if os.path.exists(se.APPLICATION_PATH + "/lib"):
		copyLibFiles()
		
	    if se.APPLICATION_ICON <> "":
		copyIconFile()
		
	    if se.APPLICATION_DESKTOP_FILE <> "":
		copyDesktopFile()
	
	    file = open(build_path +"/DEBIAN/control", 'w+')
	    file.write("Package: "+se.PACKAGE_NAME + "\n")
	    file.write("Priority: "+se.PACKAGE_PRIORITY + "\n")
	    file.write("Section: "+se.PACKAGE_SECTION + "\n")
	    file.write("Maintainer: "+se.PACKAGE_MAINTAINER + "\n")
	    file.write("Architecture: "+arch + "\n")
	    file.write("Version: "+se.PACKAGE_VERSION + "\n")
	    file.write("Depends: "+distr["depends"] + "\n")
	    file.write("Provides: "+se.PACKAGE_NAME + "\n")
	    file.write("Description: "+se.PACKAGE_DESCRIPTION + "\n")
	    file.close()

	    os.system("fakeroot dpkg-deb --build " + build_path)
