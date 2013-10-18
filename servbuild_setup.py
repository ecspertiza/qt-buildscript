VERSION = "1.0"

GIT_NAME = 'git'
GIT_REPO = 'https://ecspertiza@bitbucket.org/qb/app.git'
GIT_PATH_DOWNLOAD = './app'

SOURCE_PACKAGE_PATH = "packagepath"

APPLICATION_NAME = "app"
APPLICATION_PATH = "./app/"
APPLICATION_ICON = "app/app/images/icon_64.png"
APPLICATION_DESKTOP_FILE = "./app/install/app.desktop"
APPLICATION_PRO = "app/app.pro"
APPLICATION_MAKEFILE = "app/Makefile"

DEPENDS_PATH = "depends"
DEPENDS_PACKAGE = ["qtmobility-dev", "libqtmultimediakit1", "libopencv-dev", "libopencv-core-dev", "libopencv-imgproc-dev", "libopencv-highgui-dev", "libasound2-dev", "libquazip0-dev"]
DEPENDS_INSTALL_APP = "apt-get"

FFMPEG_NAME = "ffmpeg-0.10.7"
FFMPEG_INSTALL = True
FFMPEG_PARAM = "--disable-yasm --enable-static"

QMAKE_NAME = "qmake-qt4"

PACKAGE_NAME = "app"
PACKAGE_LICENSE = "GPL"
PACKAGE_PRIORITY = "extra"
PACKAGE_VERSION = "2.2"
PACKAGE_SECTION = "net"
PACKAGE_MAINTAINER = "company <app@support.ru>"
PACKAGE_DEPENDS_DEB = "libqt4-gui,libqt4-network,libqt4-sql,libqt4-sql-sqlite,libqt4-xml,libqt4-xmlpatterns,libqt4-declarative,libqt4-script,libopencv-imgproc2.4,libopencv-highgui2.4,libopencv-core2.4,libqtmultimediakit1,libquazip0"
PACKAGE_DEPENDS_RPM = "libqt4,libqt4-sql,libqt4-sql-sqlite,libqt4-x11,libquazip1,libopencv2_4"
PACKAGE_DEPENDS_RPM_FEDORA = "qt-x11,quazip"
PACKAGE_PACKAGER_NAME = APPLICATION_NAME + " builder " + VERSION
PACKAGE_DESCRIPTION = "app - nice application"
