import os
import servbuild_setup as se
import tarfile

if not os.path.exists(se.SOURCE_PACKAGE_PATH):
    os.makedirs(se.SOURCE_PACKAGE_PATH)

if not os.path.exists(se.SOURCE_PACKAGE_PATH + "/debbuild/"):
    os.makedirs(se.SOURCE_PACKAGE_PATH+ "/debbuild/")

if not os.path.exists(se.SOURCE_PACKAGE_PATH + "/rpmbuild/"):
    os.makedirs(se.SOURCE_PACKAGE_PATH+ "/rpmbuild/")

if not os.path.exists(se.DEPENDS_PATH):
    os.makedirs(se.DEPENDS_PATH)

if se.FFMPEG_INSTALL and not os.path.exists(se.DEPENDS_PATH+"/ffmpeg"):
    os.system("wget --directory-prefix="+se.DEPENDS_PATH+"/ffmpeg/ http://www.ffmpeg.org/releases/ffmpeg-0.10.7.tar.gz")
    
    tar = tarfile.open(se.DEPENDS_PATH+"/ffmpeg/ffmpeg-0.10.7.tar.gz")
    tar.extractall(se.DEPENDS_PATH+"/ffmpeg/")
    tar.close()
    
    os.remove(se.DEPENDS_PATH+"/ffmpeg/ffmpeg-0.10.7.tar.gz")


if not os.path.exists(se.GIT_PATH_DOWNLOAD):
    os.system(se.GIT_NAME + ' clone ' + se.GIT_REPO + ' ' + se.GIT_PATH_DOWNLOAD)
