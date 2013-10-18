import os
import servbuild_setup as se

str_install = "sudo " + se.DEPENDS_INSTALL_APP + " install "

for dep in se.DEPENDS_PACKAGE:
	str_install = str_install + dep + " "
	
os.system(str_install)