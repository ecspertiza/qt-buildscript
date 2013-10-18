import os
import servbuild_setup as se

import platform
 
arch = "i386"
 
if ("64" in platform.architecture()) or ("64bit" in platform.architecture()):
  arch = "amd64"
else:
  arch = "i386"
  
  
os.system("python download.py")
os.system("python install_depends.py")
os.system("python build_depends.py")
os.system("python build_app.py --arch " + arch)
os.system("python build_deb.py --arch " + arch)
os.system("python build_rpm.py --arch " + arch)